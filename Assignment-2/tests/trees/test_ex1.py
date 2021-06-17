import pytest
from trees.ex1 import Tree, TreeNode

def test_print(capsys):
    tree = Tree(TreeNode(1, TreeNode(7), TreeNode(17, TreeNode(6), TreeNode(3))))
    tree.print()
    capture = capsys.readouterr()
    assert "1 7 17 6 3 " in capture.out