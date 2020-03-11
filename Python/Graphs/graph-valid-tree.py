class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)

        for e in edges:
            self.graph[e[0]].append(e[1])
            self.graph[e[1]].append(e[0])


        visited = set()
        # if cycle then not a tree
        if self.hasCycle(0, visited, -1):
            return False
        # if all nodes are not connected
        if len(visited) != n:
            return False
        return True


    def hasCycle(self,node, visited, parent):

        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self.hasCycle(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False



        
