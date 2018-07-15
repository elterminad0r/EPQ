#!/usr/bin/env python3

"""
Unit tests for encode_hamming.py.

This is a testing program, that runs a series of test cases to verify that my
code works.
"""

import unittest

from decode_hamming import hamming_decode

class HammingDecodeTestCase(unittest.TestCase):
    # testing the "hamming_encode" function
    def test_hamming_encode(self):
        self.assertEqual(hamming_decode([0, 1, 1, 0, 0, 1, 1], 2), [1, 0, 1, 1])
        self.assertEqual(hamming_decode([1, 1, 1, 0, 0, 1, 1], 2), [1, 0, 1, 1])
        self.assertEqual(hamming_decode([0, 0, 1, 0, 0, 1, 1], 2), [1, 0, 1, 1])
        self.assertEqual(hamming_decode([0, 1, 1, 0, 0, 1, 0], 2), [1, 0, 1, 1])
        self.assertEqual(hamming_decode(
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], 2),
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(hamming_decode(
            [1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], 2),
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(hamming_decode(
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0], 2),
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])
        self.assertEqual(hamming_decode(
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1], 2),
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0])

if __name__ == "__main__":
    unittest.main()
