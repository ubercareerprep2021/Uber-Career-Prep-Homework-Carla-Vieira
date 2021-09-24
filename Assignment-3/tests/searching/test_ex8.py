import unittest

from searching.ex8 import *


class Ex8Test(unittest.TestCase):
    def test_count_distinct_elements(self):
        self.assertEqual(count_distinct_elements([1, 2, 1, 3, 4, 2, 3], 4), [3, 4, 4, 3])
        self.assertEqual(count_distinct_elements([1, 1, 1, 1, 2, 1, 2, 3], 3), [1, 1, 2, 2, 2, 3])
        self.assertEqual(count_distinct_elements([1, 2, 4, 4], 2), [2, 2, 1])


if __name__ == '__main__':
    unittest.main()
