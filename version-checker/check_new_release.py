#!/usr/bin/env python3

import json
import re
from typing import Optional, Tuple

import papermc_api_client
import semver
from semver import Version

# ================== GLOBALS =================================================

PROJECT = "paper"
API_BASE_URL = "https://api.papermc.io/v2"

API_CONFIGURATION = papermc_api_client.Configuration(
    host = "https://api.papermc.io"
)

# ================== TOOLS ===================================================

BASEVERSION = re.compile(
    r"""[vV]?
        (?P<major>0|[1-9]\d*)
        (\.
        (?P<minor>0|[1-9]\d*)
        (\.
            (?P<patch>0|[1-9]\d*)
        )?
        )?
    """,
    re.VERBOSE,
)

def coerce(version: str) -> Tuple[Version, Optional[str]]:
    """
    Convert an incomplete version string into a semver-compatible Version
    object

    * Tries to detect a "basic" version string (``major.minor.patch``).
    * If not enough components can be found, missing components are
        set to zero to obtain a valid semver version.

    :param str version: the version string to convert
    :return: a tuple with a :class:`Version` instance (or ``None``
        if it's not a version) and the rest of the string which doesn't
        belong to a basic version.
    :rtype: tuple(:class:`Version` | None, str)
    """
    match = BASEVERSION.search(version)
    if not match:
        return (None, version)

    ver = {
        key: 0 if value is None else value for key, value in match.groupdict().items()
    }
    ver = Version(**ver)
    rest = match.string[match.end() :]  # noqa:E203
    return ver, rest

# ================== MAIN AND FUNC============================================


def simplify_version_dict(version_dict: dict[str, list[papermc_api_client.VersionBuild]]) -> dict[str, list[str]]:
    """
        Simplify the version dict to a list of strings
        Reduce list of version contains list of Version object to list of string
        i.e:
        {
            "1.16": [..., {build: 121, ...}, {build: 122, ...}, ...],
            "1.17": [..., {build: 12, ...}, {build: 13, ...}, ...]
        }
        to
        [
            "1.16-121", "1.16-122", "1.17-12", "1.17-13"
        ]
    """
    return [f"{version}-{build.build}" for version, builds in work_versions.items() for build in builds]

def get_papermc_versions() -> list[str]:
    """
        Get all versions from PaperMC
    """
    with papermc_api_client.ApiClient(API_CONFIGURATION) as api_client:
        api_instance = papermc_api_client.ProjectControllerApi(api_client)
        try:
            project_response = api_instance.project(PROJECT)
            return project_response.versions
        except Exception as e:
            print("Exception when calling ProjectControllerApi->project: %s\n" % e)
    return []

def get_builds_for_version(version: str) -> list[papermc_api_client.VersionBuild]:
    """
        Get all builds for a version
    """
    with papermc_api_client.ApiClient(API_CONFIGURATION) as api_client:
        api_instance = papermc_api_client.VersionBuildsControllerApi(api_client)
        try:
            builds_response = api_instance.builds(PROJECT, version)
            return builds_response.builds
        except Exception as e:
            print("Exception when calling VersionControllerApi->version: %s\n" % e)
    return []

def filter_versions(versions: list[str], exclude_version_before: str) -> list[str]:
    """
        Filter versions with semver rules and exclude version before a specific
        version
    """
    selected_versions = []
    for version in versions:
        coerce_version, coerce_rest = coerce(version)
        if exclude_version_before > coerce_version:
            continue
        selected_versions.append(version)
    return selected_versions

def get_wanted_docker_versions(previous_state: dict[str, int], work_versions: dict[str, list[papermc_api_client.VersionBuild]]):
    """
        Get all versions that need to build docker image with difference from
        previous state and current state
    """
    work_versions_processed = simplify_version_dict(work_versions)
    diff_versions_to_build = list(set(work_versions_processed) - set(previous_state))
    return diff_versions_to_build

def load_last_docker_build_state():
    """"
        Load last run state from file
        last_run_state = {"build": ["M.m.p-b", "M.m.p-b", ""], "needs_build": ["M.m.p-b", "M.m.p-b", ""]}
    """
    try:
        with open("last_docker_build_state.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"build": [], "need_build": []}

def save_last_docker_build_state(last_docker_build_state):
    """"
        Save last run state to file
    """
    with open("last_docker_build_state.json", "w") as f:
        json.dump(last_docker_build_state, f)

if __name__ == "__main__":
    exclude_version_before = semver.Version.parse("1.21.4")
    # exclude_build_before = "221"

    # Load last run state from workflow
    last_docker_build_state = load_last_docker_build_state()

    # Load all versions from PaperMC
    all_versions = get_papermc_versions()

    # Filter versions with semver rules
    keep_versions = filter_versions(all_versions, exclude_version_before)

    # Get all builds for each version
    work_versions = {}
    for version in keep_versions:
        all_builds = get_builds_for_version(version)
        work_versions[version] = all_builds

    need_build_docker_versions = get_wanted_docker_versions(last_docker_build_state["build"], work_versions)
    last_docker_build_state["need_build"] = list(set(last_docker_build_state["need_build"] + need_build_docker_versions))

    # Save need_build
    save_last_docker_build_state(last_docker_build_state)

