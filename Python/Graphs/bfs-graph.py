from collections import defaultdict

class Graph:
    def __init__(self):
        self.list = defaultdict(list)
        # print(self.list)
    def addEdge(self,u,v):
        self.list[u].append(v)

    def BFS(self,start_node):
        # initialize visited list
        visited = set()

        # For BFS, queue is used
        queue = []

        # 1. Mark the node as visited and add to queue
        queue.append(start_node)
        visited.add(start_node)

        while queue:
            s = queue.pop(0) # pop 2
            print(s, end=" ")
            # add vertices which are edges to start node(2)
            for i in self.list[s]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
# g.addEdge(3, 3)
g.BFS(2)
