import pytest
from graphs.ex2 import GraphDirected


def test_dfs(capsys):
    graph = GraphDirected()
    nums = [0, 1, 2, 3]
    for x in nums:
        graph.add_node(x)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(2,0)
    graph.add_edge(2,1)
    graph.add_edge(2,3)
    graph.add_edge(3,3)
    graph.dfs(2)
    capture = capsys.readouterr()
    assert "2 0 1 3 " in capture.out