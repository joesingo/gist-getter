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

from bs4 import BeautifulSoup
import requests


BASE_URL = "https://gist.github.com"
USERNAME = "joesingo"


def get_gist_url(filename):
    response = requests.get("/".join((BASE_URL, USERNAME)))
    soup = BeautifulSoup(response.text, "html.parser")

    link = soup.find("a", string=filename)
    if not link:
        raise ValueError("Gist '{}' not found".format(filename))

    return BASE_URL + link.get("href")


def get_raw_url(gist_url):
    response = requests.get(gist_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return BASE_URL + soup.find("a", string="Raw").get("href")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: {} FILE\n".format(sys.argv[0]))
        sys.exit(1)

    try:
        gist_url = get_gist_url(sys.argv[1])
    except ValueError as ex:
        sys.stderr.write("{}: {}\n".format(sys.argv[0], ex))
        sys.exit(1)

    raw_url = get_raw_url(gist_url)
    print(requests.get(raw_url).text)
