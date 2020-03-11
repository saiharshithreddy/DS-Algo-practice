class Solution:
    def hasCycle(self, adjList):
        def dfs(node, visited):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei, visited):
                        return True
            return False

        graph = collections.defaultdict(list)
        # directed graph
        for u,v in adjList:
            graph[u].append(v)



        visited = set()
        for node in list(graph):
            dfs(node)
        visited.add(node)
if __name__ == '__main__':
    s = Solution()
    s.
