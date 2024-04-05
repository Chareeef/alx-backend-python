#!/usr/bin/env python3
"""Test client module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
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
