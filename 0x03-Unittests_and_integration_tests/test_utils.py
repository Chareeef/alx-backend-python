#!/usr/bin/env python3
"""Test utils module"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Tests for utils.access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
         """Test utils.access_nested_map results"""
         self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, error_msg):
        """Test utils.access_nested_map KeyError exception"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), error_msg)


class TestGetJson(unittest.TestCase):
    """Tests for utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expected_response, mock_get):
         """Test utils.get_json returned response"""

         # Define mocked response
         mock_get.return_value.json.return_value = expected_response

         # Call get_json
         result = get_json(url)

         # Verify that mocked get was called once with url
         mock_get.assert_called_once_with(url)

         # Verify response
         self.assertEqual(result, expected_response)
