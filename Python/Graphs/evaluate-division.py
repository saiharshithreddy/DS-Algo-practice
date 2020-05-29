# @Author: Sai Harshith
# @Date:   27-May-2020-22-05
# @Last modified by:   Sai Harshith
# @Last modified time: 27-May-2020-22-05
'''
EDGE CASE : query [x2,x4] ideal path should be x2 -> x3 -> x4, but as we are checking for all items in graph[curr] our path
will be x2->x1->x2->x3->x4 but as we keeping track of visited, our path will be x2->x1->x3->x4 which is wrong, so we have to discard the prodcut
ans = ans * item[1] by doing ans = ans / item[1] when the path we are travelling returned false and also delete the node from visited list.

TC: O(V+E)
SC: O(V)
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if len(equations) == 0:
            return

        def dfs(node, end_node, val, visited):
            # once second variable is reached and second variable is in the graph then return the result.
            # a -> b
            if node == end_node and end_node in graph:
                self.res.append(val)
                return True

            # traverse the graph
            for nei in graph[node]:

                if nei[0] not in visited:
                    val = val * nei[1]
                    visited.add(nei[0])
                    if dfs(nei[0], end_node, val, visited):
                        return True

                    else:
                        visited.remove(nei[0])
                        val = val / nei[1]
            return False


        # Build graph
        graph = collections.defaultdict(list)
        for node, val in zip(equations, values):
            graph[node[0]].append((node[1], val))
            graph[node[1]].append((node[0], 1/val))
        # print(graph)




        self.res = []

        for start, end in queries:
            # for every new query the graph has to be checked so visited has to be reset.
            visited = set()
            visited.add(start)
            # default value
            val = 1
            # if dfs returns false that means the variables of the query are not in the graph
            if not dfs(start, end, val, visited):
                self.res.append(-1)
        return self.res
