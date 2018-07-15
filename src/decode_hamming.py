#!/usr/bin/env python3

"""
Decoding Hamming-encoded data
"""

# imports the "argparse" library, which is used to interpret the parameters
# given to the program by the user
import argparse

# imports the sys library, which enables communication with other programs
import sys

# re-use the powers_to() function
from encode_hamming import powers_to, matching_indices

def get_args():
    """
    Use the argparse library to interpret user parameters:
    - What base is being used to calculate the parity?
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=int, default=2,
                            help="base to decode in")
    return parser.parse_args()

def hamming_decode(bin_stream, base):
    """
    Decode a Hamming code, correcting for a single error if present
    """
    corrupt_total = 0
    last_par = None
    for p in powers_to(len(bin_stream)):
        if sum(bin_stream[i] for i in
                            matching_indices(p, len(bin_stream))) % base:
            corrupt_total += p
            last_par = p

    if corrupt_total:
        bin_stream[corrupt_total - 1] -= sum(bin_stream[i]
                    for i in matching_indices(last_par, len(bin_stream)))
        bin_stream[corrupt_total - 1] %= base

    data = []
    powers = powers_to()
    p = next(powers)
    for ind, i in enumerate(bin_stream, 1):
        if ind != p:
            data.append(i)
        else:
            p = next(powers)

    return data

if __name__ == "__main__":
    args = get_args()
    for line in sys.stdin:
        l_code = [int(c) for c in line[:-1]]
        print("".join(map(str, hamming_decode(l_code, args.base))))
