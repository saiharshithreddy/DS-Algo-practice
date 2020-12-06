'''
Undirected graph
Logic: The number of dfs calls required to visited all nodes 
Num of connected component = 1 if every node is connected and one dfs call from the starting node will visit all nodes.
TC: O(N)
SC: O(N) for hashmap
'''

import collections
class Solution:
    def countComponents(self, n, edges):
        def dfs(node, visited):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)
        
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = 0    
        visited = set()
        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                count += 1
        
        
        
        return count
        
        
                
        