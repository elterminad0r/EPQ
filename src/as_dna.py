#!/usr/bin/env python3

"""
Convert quaternary to DNA bases ACTG, or the other way.
"""

# Translation table for quaternary to DNA
CORR = dict(zip(*(map(ord, s) for s in ("0123", "ACTG"))))

INV = {v: k for k, v in CORR.items()}

# import sys library - reading input and writing output
import sys

# import argparse library - used to get user arguments
import argparse

def get_args():
    """
    Get arguments. Determine if:
    - the user wished to convert from DNA to quaternary instead
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--inverse", action="store_true",
                            help="convert back from DNA instead")
    return parser.parse_args()

def to_dna(string):
    """
    Turn a binary string into quaternary
    """
    return string.translate(CORR)

def from_dna(string):
    """
    Turn a quaternary string into binary
    """
    return string.translate(INV)

# if called directly, transform each line of input to quaternary
if __name__ == "__main__":
    args = get_args()
    apply_func = from_dna if args.inverse else to_dna
    for line in sys.stdin:
        print(apply_func(line[:-1]))
