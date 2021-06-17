import pytest
from graphs.ex1 import GraphWithAdjacencyList


def test_add_node():
    graph = GraphWithAdjacencyList()
    graph.add_node(1)
    assert len(graph.adj_nodes) == 1
    assert graph.adj_nodes == {graph.get_node(1): []}
    graph.add_node(2)
    assert len(graph.adj_nodes) == 2
    assert graph.adj_nodes == {graph.get_node(1): [], graph.get_node(2): []}

def test_remove_node_simple():
    graph = GraphWithAdjacencyList()
    graph.add_node(1)
    assert len(graph.adj_nodes) == 1
    graph.remove_node(1)
    assert len(graph.adj_nodes) == 0

def test_remove_node_withedge():
    graph = GraphWithAdjacencyList()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1,2)
    assert len(graph.adj_nodes) == 2
    graph.remove_node(2)
    assert len(graph.adj_nodes) == 1
    assert len(graph.get_adj_nodes(1)) == 0

def test_add_edge():
    graph = GraphWithAdjacencyList()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    assert len(graph.get_adj_nodes(1)) == 1
    assert len(graph.get_adj_nodes(2)) == 1
    assert graph.get_adj_nodes(1)[0].data == 2
    assert graph.get_adj_nodes(2)[0].data == 1

def test_remove_edge():
    graph = GraphWithAdjacencyList()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    graph.remove_edge(1,2)
    assert len(graph.get_adj_nodes(1)) == 0
    assert len(graph.get_adj_nodes(2)) == 0

def test_get_adj_nodes():
    graph = GraphWithAdjacencyList()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    assert len(graph.get_adj_nodes(1)) == 2
    assert len(graph.get_adj_nodes(2)) == 1
    assert len(graph.get_adj_nodes(3)) == 2
    assert len(graph.get_adj_nodes(4)) == 1