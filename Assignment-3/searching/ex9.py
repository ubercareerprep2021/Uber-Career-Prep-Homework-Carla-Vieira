"""
Searching Exercise 9: Prefix Length
Given an array of strings arr[] and given some queries where each query
consists of a string str and an integer k. The task is to find the count of strings in arr[] whose prefix of length k
matches with the k length prefix of str.
Input: arr[] = {"abba", "abbb", "abbc", "abbd", "abaa", "abca"},
str   = "abbg", k     = 3
Output: 4
"""

# Not using trie. Time complexity: O(n*k). Space complexity: O(1).
def count_prefix_length2(arr, str, k):
    counter = 0
    for word in arr:
        if len(word) < k:
            break
        match =  True
        for i in range(k):
            if word[i] != str[i]:
                match = False
                break
        if match :
            counter += 1

    return counter


class TrieNode(object):

    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False

def add_word(root, word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node

    node.word_finished = True

def count_words_from_node(node):
    counter = 1 if node.word_finished else 0
    for child in node.children:
        counter +=  count_words_from_node(child)
    return counter

# Using Trie
def count_prefix_length(arr, str, k):
    root = TrieNode("*")
    for word in arr:
        add_word(root, word)

    node = root
    for i in range(k):
        found_in_child = False
        for child in node.children:
            if child.char == str[i]:
                node = child
                found_in_child = True
                break
        if not found_in_child:
            return 0

    return count_words_from_node(node)
