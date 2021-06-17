import pytest
from trees.ex4 import BinarySearchTree


def test_insert():
    bst = BinarySearchTree()
    nums = [16, 10, 21, 7, 13, 18, 29, 99]
    for x in nums:
        bst.insert(x)
    assert bst.root.val == 16
    assert bst.root.left.val == 10
    assert bst.root.right.val == 21
    assert bst.root.right.right.right.val == 99

def test_find():
    bst = BinarySearchTree()
    bst.insert(16)
    bst.insert(10)
    bst.insert(21)
    assert bst.find(21)
    assert not bst.find(19)
    assert bst.find(16)
