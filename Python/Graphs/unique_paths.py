# @Author: Sai Harshith
# @Date:   28-Apr-2020-12-04
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-19-05



def unique_paths(start_node, end_node):

    def dfs(node, visited, path, all_paths):

        path.append(node)

        visited.add(node)
        if node == end_node:
            all_paths.append(list(path))

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, visited, path, all_paths)
        # backtrack
        path.pop()
        visited.remove(node)


    graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
    all_paths = []
    visited = set()
    dfs(start_node, visited, [], all_paths)
    return (all_paths)

print(unique_paths('A', 'D'))
