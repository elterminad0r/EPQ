#!/usr/bin/env python3

"""
Convert binary to quaternary
"""

# Translation table for binary to quaternary
CORR = {("0", "0"): "0",
        ("0", "1"): "1",
        ("1", "0"): "2",
        ("1", "1"): "3"}

# import sys library - reading input and writing output
import sys

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

# if called directly, transform each line of input to quaternary
if __name__ == "__main__":
    for line in sys.stdin:
        print(to_quat(line[:-1]))
