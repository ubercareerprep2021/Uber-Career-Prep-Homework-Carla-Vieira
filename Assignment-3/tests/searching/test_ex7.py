import unittest

from searching.ex7 import *

class Ex7Test(unittest.TestCase):
    def test_is_pair_with_sum1(self):
        self.assertTrue(is_pair_with_sum1([0,-1,2,-3,1], -2))
        self.assertFalse(is_pair_with_sum1([1, -2, 1, 0, 5], 0))

    def test_is_pair_with_sum2(self):
        self.assertTrue(is_pair_with_sum2([0,-1,2,-3,1], -2))
        self.assertFalse(is_pair_with_sum2([1, -2, 1, 0, 5], 0))


if __name__ == '__main__':
    unittest.main()
