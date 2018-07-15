#!/usr/bin/env python3

"""
Hamming encoding framework for binary objects, using even parity.
"""

# imports the "argparse" library, which is used to interpret the parameters
# given to the program by the user
import argparse

# imports several functions that can be used to manipulate sequences - in this
# case sequences of bits
from itertools import count, takewhile, product

def get_args():
    """
    Use argparse to interpret parameters:
    - the number of bits the user wants to encode
    - if the unencoded data should be shown
    - what base should be used to calculate the parity?
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, help="bit width of codes to generate")
    parser.add_argument("--base", type=int, default=2,
                            help="base to generate codes for")
    return parser.parse_args()

def powers_to(n=float("inf")):
    """
    Get all of the powers of 2 up to a given upper limit.  Uses count() to
    produce the set of natural numbers (0, 1, 2, 3..) and takewhile() to keep
    taking powers of 2 until they exceed the limit. By default, produces all
    powers of 2.
    """
    return takewhile(lambda x: x < n, (1 << i for i in count()))

def matching_indices(power, l):
    """
    Generate the particular indices covered by a parity bit.
    """
    return (i for pstart in range(power - 1, l, power << 1)
              for i in range(pstart, min(l, pstart + power)))

def hamming_encode(bin_stream, base):
    """
    Perform Hamming encoding of a series of bits.
    """
    power = 1
    out = []

    # first fill in each index to be used for parity with [False]
    for bit in bin_stream:
        while len(out) + 1 == power:
            power <<= 1
            out.append(False)
        out.append(bit)

    # then go through each parity index and set it to the residue of the sum of
    # its data bits modulo (base)
    for power in powers_to(len(out)):
        out[power - 1] = sum(-out[i] for i in
                             matching_indices(power, len(out))) % base
    return out

def generate_codes(base, length):
    """
    Generate all codes of a given length with a given base.
    """
    # this generates all possible strings of length n, by taking the
    # cartesian product {0..base-1}^n
    for code in product(range(base), repeat=length):
        # get the encoded version and yield it
        yield hamming_encode(code, base)


# if the program is called directly, generate as many codes as the user wants.
if __name__ == "__main__":
    # uses the previous function to get the user's input
    args = get_args()
    for code in generate_codes(args.base, args.n):
        # print the encoded data to the screen
        print("".join(map(str, code)))
