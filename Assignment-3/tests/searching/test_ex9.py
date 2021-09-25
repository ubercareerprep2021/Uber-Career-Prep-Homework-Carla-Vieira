import unittest

from searching.ex9 import *

class Ex9Test(unittest.TestCase):
    def test_count_prefix_length(self):
        self.assertEqual(count_prefix_length(["abba", "abbb", "abbc", "abbd", "abaa", "abca"],"abbg", 3 ), 4)

    def test_count_prefix_length2(self):
        self.assertEqual(count_prefix_length2(["abba", "abbb", "abbc", "abbd", "abaa", "abca"],"abbg", 3 ), 4)


if __name__ == '__main__':
    unittest.main()
