#!/usr/bin/env python3

"""
Decode a set of Hadamard codes which have mutated. Applies quite a dull
brute-force approach - generate the expected matrix, and find the best matching
row by Hamming distance.
"""

import sys

import argparse

from hadamard_matrix import get_matrix

def get_args():
    """
    Use argparse to get:
    - The numbers of Hadamard iterations performed
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("iterations", type=int,
                            help="Number of iterations to perform on matrix")
    return parser.parse_args()

def hamming_distance(a, b):
    """
    Find Hamming distance between a and b
    """
    return sum(1 for i, j in zip(a, b) if i != j)

def find_best(code, mat):
    """
    Find the best matching row of a matrix wrt a given code, returning the
    index of the row, as this essentially the "id".
    """
    return min((hamming_distance(code, row), ind) for ind, row in enumerate(mat))[1]

if __name__ == "__main__":
    args = get_args()
    mat = get_matrix(args.iterations)
    for line in sys.stdin:
        print("{:0{}b}".format(find_best([int(c) for c in line[:-1]], mat),
                               args.iterations + 1))
