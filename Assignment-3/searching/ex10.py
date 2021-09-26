"""
Searching Exercise 10: Valid Words
Given a dictionary and a character array, print all valid words that are possible using characters from the array.
Input :  Dict: {"go","bat","me","eat","goal", "boy", "run"}
         arr[]: {'e','o','b', 'a','m','g', 'l'}
Output : go, me, goal.
"""

class TrieNode:

    def __init__(self,char):
        self.char = char
        self.children = []
        self.word_finished = False

def add_word(root, word):

    node = root

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

    node.word_finished = True

def explore_node_dfs(node, prefix, arr, current_list):

    if node.char not in arr: return

    new_prefix = prefix + node.char

    if node.word_finished: current_list.append(new_prefix)

    for child in node.children:
        if child.char in arr:
            explore_node_dfs(child, new_prefix, arr, current_list)


def print_trie(node):

    print("( Char: "+node.char+" Filhos: ", end="")

    for child in node.children:
        print_trie(child)

    print(")", end="")



def check_valid_words(dictionary, arr):

    root = TrieNode("*")

    for word in dictionary:
        add_word(root, word)

    ans = []


    for child in root.children:
        explore_node_dfs(child, "", arr, ans)

    return ans