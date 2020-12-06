from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    # 1. Visit one vertex, go to one of its adjacent vertex and then repeat
    def DFS(self,s):
        visited = set()
        print(self.graph)
        self.DFSUtil(s, visited)

    def DFSUtil(self, v, visited):
        if v not in visited:
            visited.add(v)
        print(v, end=" ")

        for i in self.graph[v]:
            if i not in visited:
                visited.add(i)
                self.DFSUtil(i, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
# g.addEdge(3, 3)

g.DFS(1)
