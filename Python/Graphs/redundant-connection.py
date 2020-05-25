# @Author: Sai Harshith
# @Date:   23-May-2020-13-05
# @Last modified by:   Sai Harshith
# @Last modified time: 23-May-2020-13-05


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent, visited):
            visited.add(node)

            for nei in graph[node]:
                if nei != parent:
                    if nei in visited:
                        return True
                    if dfs(nei, node, visited):
                        return True
            return False


        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            visited = set()
            if dfs(u,v, visited):
                return [u,v]

            
