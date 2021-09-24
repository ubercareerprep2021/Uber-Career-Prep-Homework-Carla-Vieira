import unittest

from searching.ex6 import *

class Ex6Test(unittest.TestCase):
    def test_isSubset1(self):
        self.assertTrue(isSubset1([11,1,13,21,3,7], [11,3,7,1]))
        self.assertTrue(isSubset1([1,2,3,4,5,6], [1,2,4]))
        self.assertFalse(isSubset1([10,5,2,23,19], [19,5,3]))

    def test_isSubset2(self):
        self.assertTrue(isSubset2([11,1,13,21,3,7], [11,3,7,1]))
        self.assertTrue(isSubset2([1,2,3,4,5,6], [1,2,4]))
        self.assertFalse(isSubset2([10,5,2,23,19], [19,5,3]))


if __name__ == '__main__':
    unittest.main()
