import unittest
from sorting.ex5 import *

class Ex5Test(unittest.TestCase):
    def test_sort_peaks_and_valleys(self):
        self.assertEqual(sort_peaks_and_valleys([5, 3, 1, 2, 3]), [5, 1, 3, 2, 3])

    def test_sort_peaks_and_valleys_size1(self):
        self.assertEqual(sort_peaks_and_valleys([5]), [5])

    def test_sort_peaks_and_valleys_size2(self):
        self.assertEqual(sort_peaks_and_valleys([5, 3]), [5, 3])

    def test_sort_peaks_and_valleys_empty(self):
        self.assertEqual(sort_peaks_and_valleys([]), [])

    def test_sort_peaks_and_valleys_equal(self):
        self.assertEqual(sort_peaks_and_valleys([5, 3, 1, 3]), [5, 1, 3, 3])


if __name__ == '__main__':
    unittest.main()
