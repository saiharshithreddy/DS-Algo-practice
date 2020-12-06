# @Author: Sai Harshith
# @Date:   06-Mar-2020-17-03
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-19-05



from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def hasCycle(self, node):
        visited = set()

        print(self.isCycle(node, visited, -1))

    def isCycle(self,node, visited, parent):

        visited.add(node)
        for nodenext in self.graph[node]:
            if(nodenext!=parent):
                if nodenext in visited:
                    return True
                if self.isCycle(nodenext,visited, node):
                    return True
        return False

g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 2)
g.hasCycle(1)
