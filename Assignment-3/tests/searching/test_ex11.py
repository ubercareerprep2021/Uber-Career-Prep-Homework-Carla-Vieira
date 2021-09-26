import unittest

from searching.ex11 import *

class Ex11Test(unittest.TestCase):
    def test_something(self):
        trie = Trie()
        trie.add_word("bad")
        trie.add_word("dad")
        trie.add_word("mad")
        self.assertFalse(trie.search("pad"))
        self.assertTrue(trie.search("bad"))
        self.assertTrue(trie.search(".ad"))
        self.assertTrue(trie.search("b.."))

if __name__ == '__main__':
    unittest.main()
