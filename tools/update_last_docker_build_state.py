#!/usr/bin/env python3

import argparse
import json
import re
from typing import Tuple, Union


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

def parse_version(version: str) -> Tuple[int, int, int, bool, Union[int, str], int]:
    """
    Parse a version and return a tuple for sorting.
    Format: major.minor.patch-build or major.minor.patch-preX-build

    Returns: (major, minor, patch, is_prerelease, pre_number, build)
    - is_prerelease: False for normal versions (higher priority)
    - pre_number: pre-release number or 0 if no pre-release
    """

    # Pattern to match different formats
    # Group 1,2,3: major.minor.patch
    # Group 4: optional “pre” + number
    # Group 5: final build number
    pattern = r'^(\d+)\.(\d+)\.(\d+)(?:-pre(\d+))?-(\d+)$'

    match = re.match(pattern, version)
    if not match:
        raise ValueError(f"Version format not recognized: {version}")

    major = int(match.group(1))
    minor = int(match.group(2))
    patch = int(match.group(3))
    pre_number = int(match.group(4)) if match.group(4) else None
    build = int(match.group(5))

    # For sorting: normal versions come AFTER pre-versions
    # for the same major.minor.patch version
    is_prerelease = pre_number is not None
    pre_sort_key = pre_number if is_prerelease else float('inf')

    return (major, minor, patch, is_prerelease, pre_sort_key, build)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load last run state from workflow")
    parser.add_argument("version", type=str, help="Build version")
    args = parser.parse_args()

    # Load last run state from workflow
    last_docker_build_state = load_last_docker_build_state()

    last_docker_build_state["build"].append(args.version)
    last_docker_build_state["need_build"].remove(args.version)

    last_docker_build_state["build"].sort(key=parse_version)
    last_docker_build_state["need_build"].sort(key=parse_version)

    save_last_docker_build_state(last_docker_build_state)