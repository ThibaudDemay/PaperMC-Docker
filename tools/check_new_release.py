#!/usr/bin/env python3

import re
from typing import Optional, Tuple

import papermc_api_client
import semver
from semver import Version

from utils import load_last_docker_build_state, parse_version, save_last_docker_build_state

# ================== GLOBALS =================================================

PROJECT = "paper"

API_CONFIGURATION = papermc_api_client.Configuration(
    host = "https://fill.papermc.io"
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


def simplify_version_dict(version_dict: dict[str, list[int]]) -> list[str]:
    """
        Simplify the version dict to a list of strings
        Reduce dict of version containing list of build numbers to list of string
        i.e:
        {
            "1.16": [121, 122, ...],
            "1.17": [12, 13, ...]
        }
        to
        [
            "1.16-121", "1.16-122", "1.17-12", "1.17-13"
        ]
    """
    return [f"{version}-{build}" for version, builds in version_dict.items() for build in builds]

def get_papermc_versions_with_builds() -> dict[str, list[int]]:
    """
        Get all versions from PaperMC with their builds using the v3 API.
        Returns a dict mapping version id to list of build numbers.
    """
    with papermc_api_client.ApiClient(API_CONFIGURATION) as api_client:
        api_instance = papermc_api_client.MetaV3Api(api_client)
        try:
            versions_response = api_instance.get_versions(PROJECT)
            return {
                v.version.id: v.builds
                for v in versions_response.versions
                if v.version and v.version.id and v.builds
            }
        except Exception as e:
            print("Exception when calling MetaV3Api->get_versions: %s\n" % e)
    return {}

def filter_versions(versions: list[str], exclude_version_before: str) -> list[str]:
    """
        Filter versions with semver rules and exclude version before a specific
        version. Also excludes pre-release versions (rc, pre, snapshot, etc.)
        as the PaperMC builds API doesn't support them.
    """
    # Pattern to detect pre-release versions (e.g., 1.21.11-rc3, 1.21-pre1)
    prerelease_pattern = re.compile(r'-(rc|pre|snapshot)', re.IGNORECASE)

    selected_versions = []
    for version in versions:
        # Skip pre-release versions
        if prerelease_pattern.search(version):
            continue
        coerce_version, coerce_rest = coerce(version)
        if exclude_version_before > coerce_version:
            continue
        selected_versions.append(version)
    return selected_versions

def get_wanted_docker_versions(previous_state: list[str], work_versions: dict[str, list[int]]) -> list[str]:
    """
        Get all versions that need to build docker image with difference from
        previous state and current state
    """
    work_versions_processed = simplify_version_dict(work_versions)
    diff_versions_to_build = list(set(work_versions_processed) - set(previous_state))
    return diff_versions_to_build


if __name__ == "__main__":
    exclude_version_before = semver.Version.parse("1.21.4")

    # Load last run state from workflow
    last_docker_build_state = load_last_docker_build_state()

    # Load all versions with builds from PaperMC v3 API
    all_versions_with_builds = get_papermc_versions_with_builds()

    # Filter versions with semver rules
    keep_versions = filter_versions(list(all_versions_with_builds.keys()), exclude_version_before)

    # Keep only filtered versions
    work_versions = {v: all_versions_with_builds[v] for v in keep_versions}

    need_build_docker_versions = get_wanted_docker_versions(last_docker_build_state["build"], work_versions)
    last_docker_build_state["need_build"] = list(set(last_docker_build_state["need_build"] + need_build_docker_versions))

    last_docker_build_state["need_build"].sort(key=parse_version)

    # Save need_build
    save_last_docker_build_state(last_docker_build_state)

