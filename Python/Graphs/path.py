# @Author: Sai Harshith
# @Date:   24-May-2020-19-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-19-05
def generate_path():

    def dfs(node, visited):
        visited.add(node)
        res.append(node)
        for nei in graph[node]:
            if nei not in visited:
                dfs(nei, visited)

        return

    graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

    res = []
    visited = set()
    dfs('A', visited)
    print(res)


generate_path()
