#!/usr/bin/env python3
"""Test client module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


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

        res = instance.org
        res = instance.org

        url = f'https://api.github.com/orgs/{org_name}'

        mock_get_json.assert_called_once_with(url)

        self.assertEqual(res, expected_response)

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
