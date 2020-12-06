'''
Approach: Topological sort
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(V+E)
Space complexity: O(V)

Algorithm:

'''

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List:
        # num of courses = num of vertices
        # prerequisites is the [u,v] (edges)

        # detect a cycle in the graph
        indegree = [0] * numCourses
        graph = defaultdict(list)
        result = []
        # create adjacency list
        for pr in prerequisites:
            # pr[1] = vertex
            # pr[0] = adj vertex
            graph[pr[1]].append(pr[0])
            indegree[pr[0]] += 1

        # push only those vertices whose indegree is 0
        queue = []

        for vertex in range(len(indegree)):
            # if indegree[i] is 0, add to queue
            if indegree[vertex] == 0:
                queue.append(vertex)

        count = 0

        while queue:
            # pop
            v = queue.pop(0)
            result.append(v)
            # check for popped vertex neighbors and decrement their indegree
            for n in graph[v]:
                indegree[n] -= 1

                if indegree[n] == 0:
                    queue.append(n)

            # as we visited a node
            count += 1
        #print(result)
        return result if count == numCourses else []
