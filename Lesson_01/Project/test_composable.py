"""
test_composable.py performs simple test of composable functions.
"""
from composable import Composable
import unittest


def reverse(s):
    "Reverses a string using negative-stride sequencing."
    return s[::-1]


def square(x):
    "Multiplies a number by itself."
    return x*x


def power(x, y):
    "Calculate (x ** y) efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x
        y >>= 1
        x = square(x)
    return number


class TestComposable(unittest.TestCase):
    def test_universe(self):
        reverser = Composable(reverse)
        nulltran = reverser * reverser
        for s in "", "0123456789", "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(nulltran(s), s)

    def test_square(self):
        squarer = Composable(square)
        po4 = squarer * square
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)

    def test_exceptions(self):
        fcs = Composable(square)
        fcp = Composable(power)
        with self.assertRaises(TypeError):
            fcs = fcs * 3
        with self.assertRaises(TypeError):
            fcs = square * fcs
        with self.assertRaises(TypeError):
            fcp = fcp**'abc'
        with self.assertRaises(ValueError):
            fcp = fcp**-3

if __name__ == "__main__":
    unittest.main()