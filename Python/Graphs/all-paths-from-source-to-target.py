class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, visited, path, all_paths):

            path.append(node)

            visited.add(node)
            if node == len(graph)-1:
                all_paths.append(list(path))

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, visited, path, all_paths)
            # backtrack
            path.pop()
            visited.remove(node)
        visited = set()
        all_paths = []
        dfs(0, visited, [], all_paths)
        
        return all_paths