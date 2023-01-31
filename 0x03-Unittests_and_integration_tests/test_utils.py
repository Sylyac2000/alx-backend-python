#!/usr/bin/env python3
"""module of unittest for utils
"""

from typing import (
    Tuple,
    Dict,
    Union,
    Any,
    Mapping,
    Sequence
)
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test case for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected_result: Union[Dict, int]) -> None:
        """Tests access_nested_map's output."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test the access_nested_map method raises an error
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
