"""
Searching Exercise 11: Add-and-Search Words
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or ‘.’. A ‘.’ means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") ⇒ false
search("bad") ⇒ true
search(".ad") ⇒ true
search("b..") ⇒ true

Note: You may assume that all words consist of lowercase letters a-z
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.finished_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word):

        node = self.root

        for char in word:
            found_in_children = False
            for child in node.children:
                if child.char == char:
                    found_in_children = True
                    node = child
                    break
            if not found_in_children:
                new_node = TrieNode(char)
                node.children.append(new_node)
                node = new_node

        node.finished_word = True

    def search(self, word):

        return self.search_dfs(self.root, word)

    def search_dfs(self, node, str):

        if not str:
            return node.finished_word

        for child in node.children:
            if str[0] == ".":
                if self.search_dfs(child, str[1:]):
                    return True
            else:
                if child.char == str[0]:
                    if self.search_dfs(child, str[1:]):
                        return True

        return False
