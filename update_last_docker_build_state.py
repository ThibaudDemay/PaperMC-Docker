#!/usr/bin/env python3

import argparse
import json


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
    parser = argparse.ArgumentParser(description="Load last run state from workflow")
    parser.add_argument("version", type=str, help="Build version")
    args = parser.parse_args()

    # Load last run state from workflow
    last_docker_build_state = load_last_docker_build_state()

    last_docker_build_state["build"].append(args.version)
    last_docker_build_state["need_build"].remove(args.version)

    last_docker_build_state["build"].sort(key=lambda x: (x.split("-")[0], int(x.split("-")[1])))
    last_docker_build_state["need_build"].sort(key=lambda x: (x.split("-")[0], int(x.split("-")[1])))

    save_last_docker_build_state(last_docker_build_state)