#!/usr/bin/env python3

"""
Unit tests for hadamard_decode.py.

This is a testing program, that runs a series of test cases to verify that my
code works.
"""

import unittest

from hadamard_decode import find_best
from hadamard_matrix import get_matrix

def make_ints(M):
    return [[int(i) for i in row] for row in M]

class HadamardDecodeTestCase(unittest.TestCase):
    # tests get_matrix
    def test_get_matrix(self):
        mat = get_matrix(4)
        self.assertEqual(find_best([1,0,0,1,0,1,1,0,0,1,1,0,1,0,1,1], mat), 0)
        self.assertEqual(find_best([1,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0], mat), 1)
        self.assertEqual(find_best([1,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0], mat), 2)
        self.assertEqual(find_best([1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0], mat), 3)
        self.assertEqual(find_best([1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0], mat), 4)
        self.assertEqual(find_best([1,1,0,0,1,1,0,0,1,0,1,0,0,0,1,1], mat), 5)
        self.assertEqual(find_best([1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1], mat), 6)
        self.assertEqual(find_best([1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0], mat), 7)
        self.assertEqual(find_best([1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0], mat), 8)
        self.assertEqual(find_best([1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1], mat), 9)

if __name__ == "__main__":
    unittest.main()
