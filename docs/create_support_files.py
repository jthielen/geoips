# # # This source code is subject to the license referenced at
# # # https://github.com/NRLMMD-GEOIPS.

"""Create the support files for versioned docs.

This includes:
- the `versions.json` file which drives the `pydata-sphinx-theme`'s version switcher
- the symlink `stable` to the latest minor release family
- a root-level `index.html` that redirects to `/stable`
- a root-level `404.html` that redirects URLs without a version string to the matching
  path on `stable`
"""

import argparse
import json
from pathlib import Path
import re
from typing import List, Dict, Union

from packaging import Version


DEFAULT_BASE_URL = "https://nrlmmd-geoips.github.io/geoips/"
BASE_VERSION_CONFIG = [
    {
        "version": "stable",
        "url": f"{BASE_URL}stable/",
        "is_latest": True
    },
    {
        "version": "dev",
        "url": f"{BASE_URL}dev/"
    },
]

"""
def get_version_list(filepath: Path) -> List[Dict]:
    with filepath.open() as f:
        output = json.load(f)
    if (
        type(output) != list
        or len(output) < 3
        or "version" not in output[0]
        or "url" not in output[0]
    ):
        raise ValueError("Invalid version JSON file specified")
    return output


def update_version_list(filepath: Path, name: str, current_list: List):
    this_version_dict = {"url": f"{BASE_URL}{name}/"}
    if name.startswith("v"):
        this_version_dict["name"] = name
        this_version_dict["version"] = name[1:]
    else:
        this_version_dict["version"] = name
    new_version_list = current_list.append(this_version_dict)
    with filepath.open("w") as f:
        json.dump(new_version_list, f)
"""

version_dir_pattern = re.compile("^v[0-9]")


def scan_for_directories(scan_path: Path) -> List[str]:
    # TODO docstring
    all_subdirs = [
        str(p.relative_to(scan_path)) for p in scan_path.iterdir() if p.is_dir()
    ]
    return [p for p in all_subdirs if version_dir_pattern.search(p)]


def create_version_config(versions: List[str], base_url: str) -> List[Dict[str, Union[str, bool]]]:
    # TODO docstring
    # Initial config, always include stable and dev
    config = [
        {
            "version": "stable",
            "url": f"{base_url}stable/",
            "is_latest": True
        },
        {
            "version": "dev",
            "url": f"{base_url}dev/"
        },
    ]
    # Now, add the directories, sorted by version
    for version_dir in sorted(versions, lambda v: Version(v[1:])):
        config.append({
            "name": version_dir,
            "version": version_dir[1:],
            "url": f"{base_url}{version_dir}/"
        })
    return config


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create support files for versioned docs"
    )

    """
    TODO:
    - args
        - `--create-version-file`
        - `--create-stable-symlink`
        - `--create-index-redirect`
        - `--create-404-redirect`
        - `--scan-dir`
        - `--output-dir`
        - `--base-url`
    """
    parser.add_argument(
        "-S",
        "--scan-dir",
        type=Path,
        help=(
            "Path containing version directories to parse (required for "
            "--create-version-file or --create-stable-symlink)"
        ),
        default=argparse.SUPPRESS
    )
    parser.add_argument(
        "-O",
        "--output-dir",
        type=Path,
        help="Output Path",
        required=True
    )
    parser.add_argument(
        "--base-url",
        type=str,
        help="Base URL to which GitHub Pages for this package deploys to",
        default=DEFAULT_BASE_URL
    )
    parser.add_argument(
        "--create-version-file",
        action="store_true",
        help="Create versions.json file in output dir"
    )
    parser.add_argument(
        "--create-stable-symlink",
        action="store_true",
        help="Create symlink `stable` to latest (non-dev) directory"
    )
    parser.add_argument(
        "--create-index-redirect",
        action="store_true",
        help="Create an index.html containing a meta-redirect to `stable`"
    )
    parser.add_argument(
        "--create-404-redirect",
        action="store_true",
        help=(
            "Create a 404.html containing JS redirect of non-versioned paths to the "
            "equivalent on `stable`"
        )
    )

    args = parser.parse_args()

    # Validate inputs
    if (
        (args.create_version_file or args.create_stable_symlink)
        and not hasattr(args, "scan_dir")
    ):
        raise ValueError((
            "Version file and/or stable symlink cannot be created without an input "
            "--scan-dir"
        ))
    if not args.base_url.endswith("/"):
        raise ValueError("--base-url must have a trailing slash to be valid")

    version_dirs = (
        scan_for_directories(args.scan_dir) if hasattr(args, "scan_dir") else None
    )

