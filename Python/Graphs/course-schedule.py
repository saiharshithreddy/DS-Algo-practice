'''
Idea: DFS with cycle detection in a directed graph. 

Cycle detection: 
1. If a node is in exploring state and the node is revisted then there is a cycle. 
2. If a node is in explored state and node is revisted means there is no cycle as all its neighbors are visited. 
TC: O(V+E) as we visit every vertex and edge. 
SC: O(V+E) for graph 
'''
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        def hasCycle(node, exploring, explored):
            
            if node in exploring:
                return True
            if node in explored:
                return False
            
            exploring.add(node)
            # Its neighbors
            for nei in self.graph[node]:
                if hasCycle(nei, exploring, explored):
                    return True
                
            explored.add(node)
            exploring.remove(node) 
            return False
        
        # create a graph
        self.graph = collections.defaultdict(list)
        for course_1, course_2 in prerequisites:
            # directed graph
            self.graph[course_1].append(course_2)
            
        
        explored = set()
        exploring = set()
        for node in list(self.graph):
            if hasCycle(node, exploring, explored):
                return False
        return True
                

# ===============================================================================

'''
Approach:

Time complexity: O(V+E)
Space complexity: O(V+E)

Algorithm:
1. Check for cycle in the directed graph
In degree concept (BFS)

'''

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
       
        # prerequisites is the [u,v] (edges)

        # detect a cycle in the graph
        # initialize every node's indegree to 0
        indegree = [0] * numCourses
        
        graph = defaultdict(list)

        # create adjacency list
        for pr in prerequisites:
            graph[pr[1]].append(pr[0])
            # as there is an edge into pr[0] its indegree is incremented. 
            indegree[pr[0]] += 1

        '''
        BFS 
        Add node to the queue only when its indegree is 0
        1. Pop nodes with indegree 0 and decrement its neighbors indegree.
        example: 1 -> 2 -> 3 
        indegree of node 1 is 0
        pop: removing the edge 1 -> 2 so indegree of 2 is decremented. 
        '''
        queue = []

        for vertex in range(len(indegree)):
            if indegree[vertex] == 0:
                queue.append(vertex)

        count = 0

        while queue:
            
            course = queue.pop(0)

            # check for popped vertex neighbors and decrement their indegree
            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)

            count += 1
        # if number of nodes popped equal to num of courses then no cycle. 
        return count == numCourses
