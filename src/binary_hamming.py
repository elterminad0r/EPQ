#4!/usr/bin/env python3


"""
Hamming encoding framework for binary objects, using even parity.
"""

# imports the "count" and "takewhile" functions
from itertools import count, takewhile

# function to get all of the powers of 2 up to a given upper limit.
# Uses count() to produce the set of natural numbers (0, 1, 2, 3..)
# and takewhile() to keep taking powers of 2 until they exceed the limit.
def powers_to(n):
    return takewhile(lambda x: x < n, (1 << i for i in count()))

# function that generates the particular indices covered by a parity bit
def matching_indices(power, l):
    return (i for pstart in range(power - 1, l, power << 1)
              for i in range(pstart, min(l, pstart + power)))

# function to Hamming encode a series of bits.
def hamming_encode(bin_stream):
    pwr = 1
    out = []

    for bit in bin_stream:
        while len(out) + 1 == pwr:
            pwr <<= 1
            out.append(False)
        out.append(bit)

    for power in powers_to(len(out)):
        out[power - 1] = 1 & sum(out[i] for i in matching_indices(power, len(out)))
    return out
