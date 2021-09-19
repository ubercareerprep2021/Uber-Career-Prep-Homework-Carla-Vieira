import unittest

from searching.ex1 import *


class Ex1Test(unittest.TestCase):
    def test_find_minimum_iterative(self):
        self.assertEqual(find_minimum_iterative([1,2,3,4]), 1)
        self.assertEqual(find_minimum_iterative([4, 1, 2, 3]), 1)
        self.assertEqual(find_minimum_iterative([2, 3, 4, 1]), 1)
        self.assertEqual(find_minimum_iterative([2, 1]), 1)
        self.assertEqual(find_minimum_iterative([1, 2]), 1)
        self.assertEqual(find_minimum_iterative([1, 1]), 1)
        self.assertEqual(find_minimum_iterative([4, 1, 1, 2, 3]), 1)
        self.assertEqual(find_minimum_iterative([1]), 1)

    def test_find_minimum_empty(self):
        with self.assertRaises(Exception):
            find_minimum_iterative([])

    def test_find_minimum_binary_search(self):
        self.assertEqual(find_minimum_binary_search([1,2,3,4]), 1)
        self.assertEqual(find_minimum_binary_search([4, 1, 2, 3]), 1)
        self.assertEqual(find_minimum_binary_search([3, 4, 1, 2]), 1)
        self.assertEqual(find_minimum_binary_search([2, 3, 4, 1]), 1)
        self.assertEqual(find_minimum_binary_search([2, 1]), 1)
        self.assertEqual(find_minimum_binary_search([1, 2]), 1)
        self.assertEqual(find_minimum_binary_search([1, 1]), 1)
        self.assertEqual(find_minimum_binary_search([4, 1, 1, 2, 3]), 1)
        self.assertEqual(find_minimum_binary_search([1]), 1)
        self.assertEqual(find_minimum_binary_search([5,6,7,8,9,1,2,3,4]), 1)
        self.assertEqual(find_minimum_binary_search([2, 2, 2, 1, 2]), 1)
        self.assertEqual(find_minimum_binary_search([2, 2, 2, 2, 2]), 2)


    def test_find_minimum_improved_empty(self):
        with self.assertRaises(Exception):
            find_minimum_binary_search([])

if __name__ == '__main__':
    unittest.main()
