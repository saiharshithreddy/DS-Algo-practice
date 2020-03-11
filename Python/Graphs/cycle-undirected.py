from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        # print(self.graph)
    def hasCycle(self, node):
        visited = set()

        print(self.dfs(node, visited, -1))

    def dfs(self,node, visited, parent):

        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                # visited.add(node)
                if self.dfs(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False

        # print(visited)

g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 2)
g.hasCycle(1)
