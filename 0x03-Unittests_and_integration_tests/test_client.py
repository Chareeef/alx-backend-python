#!/usr/bin/env python3
"""Test the Github Org client
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import itertools
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([('google',), ('abc',)])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method"""

        # Fake response
        expected_response = {org_name: 'Available'}
        mock_get_json.return_value = expected_response

        instance = GithubOrgClient(org_name)

        # Use org property
        res1 = instance.org
        res2 = instance.org

        url = f'https://api.github.com/orgs/{org_name}'

        # Ensure mocked object was called once with url
        mock_get_json.assert_called_once_with(url)

        # Verify that we got the correct payload
        self.assertEqual(res1, res2)
        self.assertEqual(res1, expected_response)

    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url method"""

        # patch GithubOrgClient.org to return a known payload
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock)\
                as org_mock:
            repos = 'https://github.com/org/test/repo'

            org_mock.return_value = {'repos_url': repos}

            # Call GithubOrgClient._public_repos_url
            org_client = GithubOrgClient('test')
            res = org_client._public_repos_url

            # Verify that we got the correct payload
            self.assertEqual(res, repos)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method"""
        repos_names = ['Tic_Tac_Toe_Python', 'alx-backend', 'simple_shell']
        repos = [{'name': name} for name in repos_names]

        mock_get_json.return_value = repos

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://github.com/test'

            # Call GithubOrgClient._public_repos_url
            org_client = GithubOrgClient('test')
            res1 = org_client.public_repos()
            res2 = org_client.public_repos()

            # Ensure mocked objects were called once
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

            # Verify that we got the correct payload
            self.assertEqual(res1, res2)
            self.assertEqual(res1, repos_names)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_response):
        """Test the GithubOrgClient.has_license static method"""

        # Test has_license with our parameters
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected_response)


@parameterized_class(
        ('org_payload', 'repos_payload',
         'expected_repos', 'apache2_repos'),
        [
            (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
             TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])
        ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get"""

        # Start requests.get patcher
        cls.get_patcher = patch('requests.get').start()

        # Define and set cyclic payloads
        cyclic_payloads = itertools.cycle([cls.org_payload,
                                           cls.repos_payload])
        cls.get_patcher.return_value.json.side_effect = cyclic_payloads

    def test_public_repos(self):
        """Integration test for GithubOrgClient.public_repos"""
        test_client = GithubOrgClient('test')

        # Test that we get the correct repos names with public_repos
        repos = test_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for GithubOrgClient.public_repos
        with the argument license="apache-2.0"
        """
        test_client = GithubOrgClient('test')

        # Test that we get the names of repos having 'apache-2.0' license
        repos = test_client.public_repos(license='apache-2.0')
        self.assertEqual(repos, self.apache2_repos)

    @classmethod
    def tearDownClass(cls):
        """Stop get_patcher"""
        cls.get_patcher.stop()
