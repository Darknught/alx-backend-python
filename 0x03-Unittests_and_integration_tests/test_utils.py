#!/usr/bin/env python3
""" A Function that test the utils.py file."""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """
    Test class for the get_json function from the utils module.
    Inherits from unittest.TestCase.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function with different inputs.

        Parameters:
        test_url (str): The URL to be passed to the get_json function.
        test_payload (dict): The expected JSON payload returned by the
        mocked requests.get.
        mock_get (Mock): The mocked requests.get method.
        """

        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function with the test URL
        result = get_json(test_url)

        # Assert that requests.get was called once with the test URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is equal to the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for the memoize function from the utils module.
    Inherits from unittest.TestCase.
    """

    def test_memoize(self):
        """
        Test the memoize decorator to ensure that the decorated
        method is called only once.
        """

        class TestClass:
            """
            A test class to demonstrate the memoize decorator.
            """

            def a_method(self):
                """
                A method that returns 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A property that calls a_method and returns its result.
                """
                return self.a_method()

        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_method:
            obj = TestClass()

            # Call a_property twice
            res1 = obj.a_property
            res2 = obj.a_property

            # Assert that a_method was called once
            mock_method.assert_called_once()

            # Assert that both results are equal to 42
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)


if __name__ == "__main__":
    unittest.main()
