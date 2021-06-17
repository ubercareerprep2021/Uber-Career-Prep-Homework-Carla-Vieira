from collections import deque

class GraphDirected:

    def __init__(self):
        self.adj_nodes = {}

    def add_node(self, key):
        self.adj_nodes[key] = []

    def remove_node(self, key):
        for node in self.adj_nodes:
            if key in self.adj_nodes[node]:
                self.adj_nodes[node].remove(key)
        self.adj_nodes.pop(key)

    def add_edge(self, key1, key2):
        self.adj_nodes[key1].append(key2)

    def remove_edge(self, key1, key2):
        self.adj_nodes[key1].remove(key2)

    def get_adj_nodes(self, key):
        return self.adj_nodes[key] if key in self.adj_nodes else None

    def bfs(self, key):
        queue = deque()
        seen = {key}
        queue.append(key)
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for adj in self.adj_nodes[node]:
                if adj not in seen:
                    seen.add(adj)
                    queue.append(adj)
        print()