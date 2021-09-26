import unittest

from searching.ex10 import *

class Ex10Test(unittest.TestCase):
    def test_check_valid_words(self):
        self.assertEqual(check_valid_words(["go","bat","me","eat","goal", "boy", "run"], {'e','o','b', 'a','m','g', 'l'}),['go', 'goal', 'me'])


if __name__ == '__main__':
    unittest.main()
