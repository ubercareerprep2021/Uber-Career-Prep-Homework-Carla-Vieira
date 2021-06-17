import pytest
from graphs.ex4 import GraphUndirected


def test_min_number_of_edges():
    graph = GraphUndirected()
    for x in range(7):
        graph.add_node(x)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    assert graph.min_number_of_edges(1,5) == 2
    assert graph.min_number_of_edges(6, 1) == 3

def test_min_number_of_edges_bidirectional():
    graph = GraphUndirected()
    for x in range(7):
        graph.add_node(x)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    assert graph.min_number_of_edges_bidirectional(1,5) == 2
    assert graph.min_number_of_edges_bidirectional(6, 1) == 3