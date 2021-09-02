import unittest

from searching.ex5 import *

class Ex5Test(unittest.TestCase):
    def test_something(self):
        matrix = [[1, 4, 7, 11, 15],
                  [2, 5, 8, 12, 19],
                  [3, 6, 9, 16, 22],
                  [10, 13, 14, 17, 24],
                  [18, 21, 23, 26, 30]]

        self.assertTrue(is_in_matrix(matrix, 24))
        self.assertTrue(is_in_matrix(matrix, 1))
        self.assertTrue(is_in_matrix(matrix, 30))
        self.assertTrue(is_in_matrix(matrix, 18))
        # self.assertTrue(is_in_matrix(matrix, 22))
        # self.assertTrue(is_in_matrix(matrix, 3))
        #
        # self.assertFalse(is_in_matrix(matrix, 20))
        # self.assertFalse(is_in_matrix(matrix, 50))
        # self.assertFalse(is_in_matrix(matrix, -2))


if __name__ == '__main__':
    unittest.main()
