#!/usr/bin/env python3

"""
Translate quaternary to binary
"""

# sys library, for reading input and writing output
import sys

# import the translation table from to_quat
from to_quat import CORR

# reverse the translation table
REV = {v: k for k, v in CORR.items()}

def to_binary(string):
    """
    Translate a string to binary
    """
    return "".join("".join(REV[c]) for c in string)

# if called directly, translate each line of input to binary
if __name__ == "__main__":
    for line in sys.stdin:
        print(to_binary(line[:-1]))
