import unittest

from searching.ex1 import *


class Ex1Test(unittest.TestCase):
    def test_find_minimum(self):
        self.assertEqual(find_minimum([1,2,3,4]), 1)
        self.assertEqual(find_minimum([4, 1, 2, 3]), 1)
        self.assertEqual(find_minimum([2, 3, 4, 1]), 1)
        self.assertEqual(find_minimum([2, 1]), 1)
        self.assertEqual(find_minimum([1, 2]), 1)
        self.assertEqual(find_minimum([1, 1]), 1)
        self.assertEqual(find_minimum([4, 1, 1, 2, 3]), 1)
        self.assertEqual(find_minimum([1]), 1)

    def test_find_minimum_empty(self):
        with self.assertRaises(Exception):
            find_minimum([])

    def test_find_minumum_improved(self):
        self.assertEqual(find_minimum_improved([1,2,3,4]), 1)
        self.assertEqual(find_minimum_improved([4, 1, 2, 3]), 1)
        self.assertEqual(find_minimum_improved([3, 4, 1, 2]), 1)
        self.assertEqual(find_minimum_improved([2, 3, 4, 1]), 1)
        self.assertEqual(find_minimum_improved([2, 1]), 1)
        self.assertEqual(find_minimum_improved([1, 2]), 1)
        self.assertEqual(find_minimum_improved([1, 1]), 1)
        self.assertEqual(find_minimum_improved([4, 1, 1, 2, 3]), 1)
        self.assertEqual(find_minimum_improved([1]), 1)
        self.assertEqual(find_minimum_improved([5,6,7,8,9,1,2,3,4]), 1)
        self.assertEqual(find_minimum_improved([2, 2, 2, 1, 2]), 1)


    def test_find_minimum_improved_empty(self):
        with self.assertRaises(Exception):
            find_minimum_improved([])

if __name__ == '__main__':
    unittest.main()
