import logging
import os

import requests

log = logging.getLogger(__name__)

year = 2025


def get_token():
    """Load the user's token from session.txt"""
    with open("session.txt") as file:
        return str(file.read()).strip()


def download(day: int, year: int = year):
    log.debug(f"Downloading {year}/{day}")
    token = get_token()
    headers = {"cookie": token}
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", headers=headers
    )
    return response.text


def input(day: int):
    """Get input for day 'n', downloading if necessary"""
    path = f"input{day:02}.txt"
    if os.path.exists(path):
        with open(path, "r") as file:
            log.debug(f"Reading input for day {day} from {file.name}")
            return str(file.read())
    else:
        with open(path, "w") as file:
            input = download(day)
            log.debug(f"Saving input for day {day} as {file.name}")
            file.write(input)
            return input


def split(input: str):
    """Splint the input into lines"""
    return input.split(sep="\n")
