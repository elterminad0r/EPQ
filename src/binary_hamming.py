#!/usr/bin/env python3


"""
Hamming encoding framework for binary objects, using even parity.
"""

from itertools import count, takewhile

def powers_to(n):
    return takewhile(lambda x: x < n, (1 << i for i in count()))

def matching_indices(power, l):
    return (i for pstart in range(power - 1, l, power << 1)
              for i in range(pstart, min(l, pstart + power)))

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
