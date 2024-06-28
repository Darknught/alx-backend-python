#!/usr/bin/env python3
""" A Function that test the utils.py file."""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for the access_nested_map function from the utils module.
    Inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with different inputs.
        Parameters:
        nested_map (Mapping): The nested map to access.
        path (Sequence): The sequence of keys representing the path to
        the value.
        expected (Any): The expected result from the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception):
        """
        Test the access_nested_map function to ensure it raises
        KeyError for invalid paths.

        Parameters:
        nested_map (Mapping): The nested map to access.
        path (Sequence): The sequence of keys representing the
        path to the value.
        expected_exception (str): The expected exception message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_exception)


if __name__ == "__main__":
    unittest.main()
