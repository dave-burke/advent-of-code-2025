#!/bin/env python3

import logging

import aoc

logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__name__)


def part1(input: str):
    log.debug("Running part 1...")
    print(input)


if __name__ == "__main__":
    input = aoc.input(1)
    part1(input)
