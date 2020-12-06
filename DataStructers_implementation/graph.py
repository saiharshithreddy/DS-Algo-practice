class AdjNode:
    def __init__(self, val):
        self.vertex = val
        self.next = None


class Graph:
    def __init__(self,V,E):
        self.V = V
        self.list = [None] * self.V

    def add_edge(self, src, dest):
        # create a node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.list[src] = node

        # undirected Graph
        node = AdjNode(src)
        node.next = self.list[dest]
        self.list[dest] = node

    
