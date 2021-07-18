import unittest
from sorting.ex4 import *

class Ex4Test(unittest.TestCase):
    def test_group_anagrams(self):
        self.assertEqual(group_anagrams(["abc", "efc", "ggg", "bca", "cfe", "cba"]), ['abc', 'bca', 'cba', 'efc', 'cfe', 'ggg'])

    def test_group_anagrams_empty(self):
        self.assertEqual(group_anagrams([]), [])


if __name__ == '__main__':
    unittest.main()
