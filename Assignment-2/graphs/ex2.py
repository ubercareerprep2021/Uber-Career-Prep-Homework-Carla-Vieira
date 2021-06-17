class GraphDirected:

    def __init__(self):
        self.adj_nodes = {}

    def add_node(self, key):
        self.adj_nodes[key] = []

    def remove_node(self, key):
        adjacents = self.adj_nodes[key]
        for adjacent in adjacents:
            self.adj_nodes[adjacent].remove(key)
        self.adj_nodes.pop(key)

    def add_edge(self, key1, key2):
        self.adj_nodes[key1].append(key2)

    def remove_edge(self, key1, key2):
        self.adj_nodes[key1].remove(key2)

    def get_adj_nodes(self, key):
        return self.adj_nodes[key] if key in self.adj_nodes else None

    def dfs(self, key):
        self.dfs_recursive(key, set())
        print()

    def dfs_recursive(self, key, seen):
        print(key, end=" ")
        seen.add(key)
        for node in self.get_adj_nodes(key):
            if node not in seen:
                self.dfs_recursive(node, seen)