#!/usr/bin/env python3
""" Module to Test the GithubOrgClient class"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient.

        Parameters:
        mock_get_json (Mock): The mocked get_json method.
        """
        test_payload = [
                {"name": "repo1", "license": {"key": "mit"}},
                {"name": "repo2", "license": {"key": "apache-2.0"}},
                {"name": "repo3", "license": {"key": "mit"}},
        ]
        mock_get_json.return_value = test_payload

        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                    "https://api.github.com/orgs/test_org/repos")

            # Create an instance of GithubOrgClient with test organization name
            client = GithubOrgClient("test_org")

            # Call the public_repos method
            result = client.public_repos()

            # Assert that the result is the list of repo names
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            # Assert that _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

            # assert that get_json was called once with expected url
            mock_get_json.assert_called_once_with(
                    "https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method of GithubOrgClient.

        Parameters:
        repo (dict): The repository data.
        license_key (str): The license key to check.
        expected (bool): The expected result.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
