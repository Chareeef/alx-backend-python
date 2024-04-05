#!/usr/bin/env python3
"""Test utils module"""
from parameterized import parameterized
import unittest
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
