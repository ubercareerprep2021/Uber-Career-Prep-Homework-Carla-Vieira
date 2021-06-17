from collections import deque

class GraphUndirected:

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
        self.adj_nodes[key2].append(key1)

    def remove_edge(self, key1, key2):
        self.adj_nodes[key1].remove(key2)
        self.adj_nodes[key2].remove(key1)

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


    def min_number_of_edges(self, node1, node2):
        queue = deque()
        seen = {node1}
        queue.append((node1, 0))
        while queue:
            current_node, level = queue.popleft()
            print(node1, node2, current_node, level)
            if current_node == node2:
                return level
            for adj in self.adj_nodes[current_node]:
                if adj not in seen:
                    seen.add(adj)
                    queue.append((adj, level+1))
        raise Exception("No connection found")


    def min_number_of_edges_bidirectional(self, node1, node2):
        queue1, queue2 = deque(), deque()
        seen1, seen2 = {node1:0}, {node2:0}
        queue1.append((node1, 0))
        queue2.append((node2, 0))
        while (queue1 or queue1):
            if queue1: current1, level1 = queue1.popleft()
            if queue2: current2, level2 = queue2.popleft()
            print(current1, level1, "---", current2, level2)
            if current1 in seen2:
                return level1 + seen2[current1]
            if current2 in seen1:
                return level2 + seen1[current2]
            for adj in self.adj_nodes[current1]:
                if adj not in seen1:
                    seen1[adj] = level1 + 1
                    queue1.append((adj, level1+1))
            for adj in self.adj_nodes[current2]:
                if adj not in seen2:
                    seen2[adj] = level2 + 1
                    queue2.append((adj, level2+1))
