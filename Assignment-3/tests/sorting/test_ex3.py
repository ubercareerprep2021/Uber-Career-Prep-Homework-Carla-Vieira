import unittest

from sorting.ex3 import *

class Ex3Test(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([3,5,7,0,0,0,0], [1,2,4,6], 3), [1,2,3,4,5,6,7])
        self.assertEqual(merge_sorted_arrays([1,2,4,6,0,0,0], [3,5,7], 4), [1,2,3,4,5,6,7])

    def test_merge_sorted_arrays_noB(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 4, 6], [], 4), [1, 2, 4, 6])

    def test_merge_sorted_arrays_noA(self):
        self.assertEqual(merge_sorted_arrays([0, 0, 0, 0], [1, 2, 4, 6], 0), [1, 2, 4, 6])

    def test_merge_sorted_arrays_noAB(self):
        self.assertEqual(merge_sorted_arrays([], [], 0), [])


if __name__ == '__main__':
    unittest.main()
