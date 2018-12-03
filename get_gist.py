#!/usr/bin/env python3
"""
Small script to print the latest version of a GitHub Gist given a filename.
If the gist contains several files only the first one is returned.

Only works for publicly-accessible gists, and the username is hardcoded at the
top of the script.

Requirements can be installed with

  pip3 install beautifulsoup4 requests

and the script is run as

    ./get_gist.py <filename>
"""
import sys

import requests


API_URL = "https://api.github.com"
USERNAME = "joesingo"


def get_raw_url(filename):
    """
    Return raw URL for a file within a gist. Raises ValueError if file is not
    found.
    """
    resp = requests.get("{base}/users/{user}/gists".format(
        base=API_URL,
        user=USERNAME
    )).json()

    if "message" in resp:
        raise ValueError("Error listing gists. Message from API is: {}".format(
            resp["message"]
        ))

    for obj in resp:
        if filename in obj["files"]:
            return obj["files"][filename]["raw_url"]

    raise ValueError("File '{}' not found for user '{}'".format(
        filename, USERNAME
    ))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: {} FILE\n".format(sys.argv[0]))
        sys.exit(1)

    try:
        raw_url = get_raw_url(sys.argv[1])
    except ValueError as ex:
        sys.stderr.write("{}: {}\n".format(sys.argv[0], ex))
        sys.exit(1)

    print(requests.get(raw_url).text)
