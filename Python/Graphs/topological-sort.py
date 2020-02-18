'''
1. a vertex is pushed to stack only when all of its adjacent vertices
(and their adjacent vertices and so on) are already in stack.


Time complexity: O(V+E)
Space complexity: O(V)

Algorithm:
1. Visit one vertex and then recursively visit its neighbors
2. Push the neighbor which has no more neighbors into the stack
3. Do it for all vertices

'''
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u,v):
        self.graph[u].append(v)


    def topologicalUtil(self,v,visited,result):
        # set vertex as visited
        visited[v] = True
        
        # look for its adjacent vertices
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalUtil(i,visited,result)

        result.insert(0,v)


    def topological_sort(self):
        visited = [False] * self.V
        result = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalUtil(i,visited, result)
        print(result)

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);


g.topological_sort()
