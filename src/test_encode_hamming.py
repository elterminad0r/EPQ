#!/usr/bin/env python3

"""
Unit tests for encode_hamming.py.

This is a testing program, that runs a series of test cases to verify that my
code works.
"""

import unittest

from encode_hamming import powers_to, hamming_encode, matching_indices

class HammingEncodeTestCase(unittest.TestCase):
    # testing the "powers_to" function
    def test_powers_to(self):
        self.assertEqual(list(powers_to(0)), [])
        self.assertEqual(list(powers_to(1)), [])
        self.assertEqual(list(powers_to(2)), [1])
        self.assertEqual(list(powers_to(4)), [1, 2])
        self.assertEqual(list(powers_to(5)), [1, 2, 4])
        self.assertEqual(list(powers_to(13)), [1, 2, 4, 8])

    # testing the "hamming_encode" function
    def test_hamming_encode(self):
        self.assertEqual(hamming_encode([1, 0, 1, 1], 2), [0, 1, 1, 0, 0, 1, 1])
        self.assertEqual(hamming_encode(
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0], 2),
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])

    # testing the "matching_indices" function
    def matching_indices(self):
        self.assertEqual(matching_indices(1, 7), [1, 3, 5, 7])
        self.assertEqual(matching_indices(2, 7), [2, 3, 6, 7])
        self.assertEqual(matching_indices(4, 7), [4, 5, 6, 7])
        self.assertEqual(matching_indices(4, 1), [])
        self.assertEqual(matching_indices(1, 1), [1])
        self.assertEqual(matching_indices(1, 2), [1])
        self.assertEqual(matching_indices(4, 5), [4, 5])

if __name__ == "__main__":
    unittest.main()
