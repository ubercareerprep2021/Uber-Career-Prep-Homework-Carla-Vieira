class GraphNode:

    def __init__(self, data):
        self.data = data


class GraphWithAdjacencyList:

    def __init__(self):
        self.adj_nodes = {}

    def add_node(self, key):
        self.adj_nodes[GraphNode(key)] = []

    def remove_node(self, key):
        for node in self.adj_nodes:
            if node.data == key:
                to_remove = node
                adjacents = self.adj_nodes[node]
        self.adj_nodes.pop(to_remove)
        for adjacent in adjacents:
            self.adj_nodes[adjacent].remove(to_remove)

    def get_node(self, key):
        for node in self.adj_nodes:
            if node.data == key:
                return node
        raise Exception("Node not found")

    def add_edge(self, key1, key2):
        node1, node2 = self.get_node(key1), self.get_node(key2)
        self.adj_nodes[node1].append(node2)
        self.adj_nodes[node2].append(node1)

    def remove_edge(self, key1, key2):
        node1, node2 = self.get_node(key1), self.get_node(key2)
        self.adj_nodes[node1].remove(node2)
        self.adj_nodes[node2].remove(node1)

    def get_adj_nodes(self, key):
        for node in self.adj_nodes:
            if node.data == key:
                return self.adj_nodes[node]
        return None