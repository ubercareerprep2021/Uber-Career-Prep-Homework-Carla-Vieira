import pytest
from graphs.ex3 import GraphDirected


def test_bfs(capsys):
    graph = GraphDirected()
    nums = [0, 1, 2, 3]
    for x in nums:
        graph.add_node(x)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(2,0)
    graph.add_edge(2,3)
    graph.add_edge(3,3)
    graph.bfs(2)
    capture = capsys.readouterr()
    assert "2 0 3 1 " in capture.out