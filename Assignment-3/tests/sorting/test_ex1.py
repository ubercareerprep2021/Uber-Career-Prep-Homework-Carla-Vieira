import unittest

from sorting.ex1 import *

class TestEx1(unittest.TestCase):
    def test_three_partition_sort(self):
        self.assertEqual(three_partition_sort([5, 10, 5, 20, 5, 5, 10], 10), [5, 5, 5, 5, 10, 10, 20])
        self.assertEqual(three_partition_sort([3, 2, 3, 2, 0.5, 2, 3, 0.5], 2), [0.5, 0.5, 2, 2, 2, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()