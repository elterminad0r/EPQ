#!/usr/bin/env python3

"""
Hamming encoding framework for binary objects, using even parity.
"""

from itertools import count, takewhile

def powers_to(n):
    return takewhile(lambda x: x < n, (1 << i for i in count()))

def hamming_encode(bin_stream):
    pwr = 1
    out = []

    for bit in bin_stream:
        while len(out) + 1 == pwr:
            pwr <<= 1
            out.append(0)
        out.append(bit)

    for i in powers_to(len(out)):
        out[i - 1] = 1 & sum(out[pbit] for pstart in range(i - 1, len(out), i << 1)
                                       for pbit in range(pstart, pstart + i))
    return out
