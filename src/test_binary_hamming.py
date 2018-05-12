"""
Unit tests for binary_hamming.py.

This is a testing program, that runs a series of test cases to verify that my
code works.
"""

import unittest

from binary_hamming import powers_to, hamming_encode

class BinaryHammingTestCase(unittest.TestCase):
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
        self.assertEqual(hamming_encode([1, 0, 1, 1]), [0, 1, 1, 0, 0, 1, 1])
        self.assertEqual(hamming_encode(
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]),
            [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])

if __name__ == "__main__":
    unittest.main()
