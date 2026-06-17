#!/usr/bin/env python3

import argparse

from utils import load_last_docker_build_state, parse_version, save_last_docker_build_state

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