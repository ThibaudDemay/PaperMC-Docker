# coding: utf-8

"""
    PaperMC API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from papermc_api_client.api.version_family_builds_controller_api import VersionFamilyBuildsControllerApi


class TestVersionFamilyBuildsControllerApi(unittest.TestCase):
    """VersionFamilyBuildsControllerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VersionFamilyBuildsControllerApi()

    def tearDown(self) -> None:
        pass

    def test_family_builds(self) -> None:
        """Test case for family_builds

        Gets all available builds for a project's version group.
        """
        pass


if __name__ == '__main__':
    unittest.main()
