import unittest

from searching.ex2 import *

class Ex2Test(unittest.TestCase):
    def test_find_element(self):
        self.assertEqual(find_element([1,2,3,4], 1), 0)
        self.assertEqual(find_element([4, 5, 6, 1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(find_element([1, 2, 1, 1, 1, 1, 1, 1], 2), 1)
        self.assertEqual(find_element([2, 2, 2, 2, 2, 1, 2, 2], 1), 5)
        self.assertEqual(find_element([2, 2, 2, 2, 2, 2, 2, 2], 2), 3)
        self.assertEqual(find_element([2, 2, 1, 2, 2, 2, 2, 2], 1), 2)

    def test_find_element_empty(self):
        with self.assertRaises(Exception):
            find_element([])

    def test_find_element_not_present(self):
        with self.assertRaises(Exception):
            find_element([1,2,3,4], 5)
        with self.assertRaises(Exception):
            find_element([2, 2, 2, 2, 2, 2, 2, 2], 1)


if __name__ == '__main__':
    unittest.main()
