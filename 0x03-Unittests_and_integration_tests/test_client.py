#!/usr/bin/env python3
""" Module to Test the GithubOrgClient class"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient class from the client module.
    Inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("google", {
            "name": "Google", "repos_url":
            "https://api.github.com/orgs/google/repos"}),
        ("abc", {
            "name": "ABC", "repos_url":
            "https://api.github.com/orgs/abc/repos"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected_response, mock_get_json):
        """
        Test the org method of GithubOrgClient.

        Parameters:
        org_name (str): The organization name to pass to GithubOrgClient.
        expected_response (dict): The expected JSON response from
        the mocked get_json.
        mock_get_json (Mock): The mocked get_json method.
        """

        # Set the return value of the mock
        mock_get_json.return_value = expected_response

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Assert that get_json was called once with expected URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")

        # Assert that the result is equal to the expected response
        self.assertEqual(result, expected_response)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test the _public_repos_url property of GithubOrgClient.

        Parameters:
        mock_org (PropertyMock): The mocked org property.
        """
        mock_payload = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"}
        mock_org.return_value = mock_payload

        # Create an instance of GithubOrgClient with a test organization name
        client = GithubOrgClient("test_org")

        # Access the _public_repos_url property
        result = client._public_repos_url

        # assert that the result is equal to the expected repos_url
        self.assertEqual(result, mock_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
