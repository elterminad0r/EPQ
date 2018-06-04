#!/usr/bin/env python3

"""
Unit tests for hadamard_matrix.py.

This is a testing program, that runs a series of test cases to verify that my
code works.
"""

import unittest

from hadamard_matrix import hadamard_iterate, get_matrix

def make_ints(M):
    return [[int(i) for i in row] for row in M]

class HadamardMatrixTestCase(unittest.TestCase):
    # tests hadamard_iterate
    def test_hadamard_iterate(self):
        mat = [[1]]; hadamard_iterate(mat)
        self.assertEqual(mat,
            [[1, 0],
             [1, 1]])
        mat = [[0]]; hadamard_iterate(mat)
        self.assertEqual(mat,
            [[0, 1],
             [0, 0]])
        mat = [[1, 0],
               [0, 1]]; hadamard_iterate(mat)
        self.assertEqual(mat,
           [[1, 0, 0, 1],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1]])

    # tests get_matrix
    def test_get_matrix(self):
        self.assertEqual(make_ints(get_matrix(0)),
            [[1],
             [0]])
        self.assertEqual(make_ints(get_matrix(1)),
            [[1, 0],
             [1, 1],
             [0, 1],
             [0, 0]])

if __name__ == "__main__":
    unittest.main()
