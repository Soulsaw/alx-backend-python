#!/usr/bin/env python3
"""
Doc of the module test_utils
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
"""
Import module documented here
"""


class TestAccessNestedMap(unittest.TestCase):
    """Doc of the unittest class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ('a',), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cmd:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cmd.exception), str(KeyError(path[-1])))


if __name__ == "__main__":
    """Call of the main function"""
    unittest.main()
