#!/usr/bin/env python3

"""
Program that simulates the application of "mutations" to nucleotide data
"""

# imports the "argparse" library, which is used to interpret user parameters.
import argparse

# imports the sys library, which enables communication with other programs
import sys

# imports the "random" library, which is used to generate random mutations.
from random import sample, choice

def get_args():
    """
    Parse user parameters:
    - How many mutations should be applied?
    - Where should output data be written to?
    - How many bases are being simulated?
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", type=int, default=1, help="number of mutations")
    parser.add_argument("--base", type=int, default=4, help="number of bases")
    return parser.parse_args()

def mutate(string, base, n, alphabet):
    """
    Apply n random mutations to a string with some number of bases, given an
    alphabet of mutatable targets.
    """
    inds = sample(range(len(string)), n)
    inds.sort()
    out_string = []
    cur_pos = 0
    for i in inds:
        out_string.append(string[cur_pos:i])
        out_string.append(choice(alphabet))
        cur_pos = i + 1
    out_string.append(string[cur_pos:])
    return "".join(out_string)

# if called directly, apply mutations to input
if __name__ == "__main__":
    args = get_args()
    alphabet = list(map(str, range(args.base)))
    for line in sys.stdin:
        print(mutate(line[:-1], args.base, args.n, alphabet))
