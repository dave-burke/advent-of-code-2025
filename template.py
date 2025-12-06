#!/bin/env python3

import logging

import aoc

logging.basicConfig(level=logging.WARN)
log = logging.getLogger(__name__)

dayNum = 1


def part1(input: str):
    log.debug("Running part 1...")
    print(input)


if __name__ == "__main__":
    input = aoc.input(dayNum)
    part1(input)
