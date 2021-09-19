import unittest

from searching.ex3 import *

class Ex3Test(unittest.TestCase):
    def test_pow_recursive(self):
        self.assertEqual(pow_recursive(2,6), 64)
        self.assertEqual(pow_recursive(3,9), 19683)
        self.assertEqual(pow_recursive(2, -4), 0.0625)

    def test_pow_iterative(self):
        self.assertEqual(pow_iterative(2,6), 64)
        self.assertEqual(pow_iterative(3,9), 19683)
        self.assertEqual(pow_iterative(2, -4), 0.0625)


if __name__ == '__main__':
    unittest.main()
