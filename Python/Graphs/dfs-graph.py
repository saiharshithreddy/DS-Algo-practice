from collections import defaultdict

class Graph:
    def __init__(self):
        self.list = defaultdict(list)
        print(self.list)
    def addEdge(self,u,v):
        self.list[u].append(v)

    # 1. Visit one vertex, go to one of its adjacent vertex and then repeat
    def DFS(self,s):
        visited = [False] * len(self.list)

        self.DFSUtil(s, visited)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.list[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)







g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(1)
