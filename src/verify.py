#!/usr/bin/env python2

"""
Verifies that the input is in (lexicographical) ascending order
"""

# imports "sys" library, used to either exit cleanly or display that there is a
# problem
import sys

# imports "argparse" library, used to parse user parameters
import argparse

def get_args():
    """
    Parse user parameters:
    - Where should data be read from?
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=argparse.FileType("r"), default="-",
                            help="file to verify data from")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    cur_line = next(args.input)
    for line in args.input:
        if cur_line > line:
            print("error: {!r} > {!r}".format(cur_line, line))
            sys.exit(1)
        cur_line = line
