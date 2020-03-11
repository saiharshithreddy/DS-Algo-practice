'''
Approach: DFS
Time complexity: O()
Space complexity: O()

Algorithm:
1. Check the number of times dfs is called.
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, visited):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited)

        count = 0
        visited = set()
        # call dfs
        for i in range(n):
            if i not in visited: # to call only if the node is unvisited
                dfs(i, visited)
                count += 1


        return count
