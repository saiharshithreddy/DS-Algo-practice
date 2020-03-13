'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()

Algorithm:
1. BFS and color neighbors with different colors
2. Handle disjoint graphs so call BFS on every node
'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # graph coloring
        def BFS(node):
            queue = []

            color[node] = 0
            queue.append(node)
            while queue:
                n = queue.pop(0)
                c = color[n]
                for nei in graph_struct[n]:

                    if color[nei] == c:
                        return False
                    if color[nei] == -1 and color[nei] != c:
                        queue.append(nei)
                        color[nei] = 1-c
            return True


        graph_struct = collections.defaultdict()
        color = {}
        
        for i in range(len(graph)):
            graph_struct[i] = graph[i]
            color[i] = -1

        vertices = list(graph_struct.keys())
        start_node = 0


        for i in range(len(vertices)):
            # if node is not visted, color will be -1
            if color[i] == -1:
                if not BFS(i): # return only if BFS returns False
                    return False

        return True
