"""
Test list-of-list-of-list based on array implementation.
"""
from arr import Array
import unittest


class TestArray(unittest.TestCase):
    def test_zeroes(self):
        for N in range(10):
            a = Array(N, N, N)
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[k, i, j], 0)

    def test_identity(self):
        for N in range(10):
            a = Array(N, N, N)
            for i in range(N):
                a[i, i, i] = 1
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        self.assertEqual(a[k, i, j], i == j == k)

    def _index(self, a, p, r, c):
        return a[p, r, c]

    def test_key_validity(self):
        a = Array(10, 10, 10)
        self.assertRaises(KeyError, self._index, a, -1, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, -1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, -1)
        self.assertRaises(KeyError, self._index, a, 10, 1, 1)
        self.assertRaises(KeyError, self._index, a, 1, 10, 1)
        self.assertRaises(KeyError, self._index, a, 1, 1, 10)

if __name__ == "__main__":
    unittest.main()