import unittest

from searching.ex4 import *

class Ex4Test(unittest.TestCase):
    def test_find_median_recursive(self):
        self.assertEqual(find_median_recursive([1, 2, 7, 8, 11], [3, 5, 9, 10, 12]), 7.5)
        self.assertEqual(find_median_recursive([1, 2, 7, 8, 11], [3, 5, 10, 12]), 7)

    # def test_find_median_iterative(self):
    #     self.assertEqual(find_median_iterative([1, 2, 7, 8, 11], [3, 5, 9, 10, 12]), 7.5)
    #     self.assertEqual(find_median_iterative([1, 2, 7, 8, 11], [3, 5, 10, 12]), 7)


if __name__ == '__main__':
    unittest.main()
