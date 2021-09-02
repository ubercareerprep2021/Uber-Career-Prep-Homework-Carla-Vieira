import unittest
import random

from sorting.ex2 import *

class Ex2Test(unittest.TestCase):
    def test_load_entries(self):
        numbers = [random.randint(1, 1000) for _ in range(10 ** 3)]
        self.assertTrue(load_entries(numbers).sorted())


if __name__ == '__main__':
    print("teste")
    unittest.main()
