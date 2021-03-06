#!/usr/bin/env python3

"""
Convert binary to quaternary
"""

# Translation table for binary to quaternary
CORR = {("0", "0"): "0",
        ("0", "1"): "1",
        ("1", "0"): "2",
        ("1", "1"): "3"}

# reverse the translation table
REV = {v: k for k, v in CORR.items()}

# import sys library - reading input and writing output
import sys

# import argparse library - used to get user arguments
import argparse

def get_args():
    """
    Get arguments. Determine if:
    - the user wished to convert from quaternary to binary, instead
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--inverse", action="store_true",
                            help="convert back from DNA instead")
    return parser.parse_args()

def chunk(it, n):
    """
    Split a sequence into chunks - in this case used to split binary into pairs
    of bits
    """
    return zip(*[iter(it)] * n)

def to_quat(string):
    """
    Turn a binary string into quaternary
    """
    return "".join(CORR[ch] for ch in chunk(string, 2))

def to_binary(string):
    """
    Translate a string to binary
    """
    return "".join("".join(REV[c]) for c in string)

# if called directly, transform each line of input to quaternary
if __name__ == "__main__":
    args = get_args()
    apply_func = to_binary if args.inverse else to_quat
    for line in sys.stdin:
        print(apply_func(line[:-1]))
