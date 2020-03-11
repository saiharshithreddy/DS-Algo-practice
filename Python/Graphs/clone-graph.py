"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()

Algorithm:
1. Using BFS, clone each node in the graph. Store the map between old_node and new node
2. Iterate through the hashmap and update the neighbors of the new nodes by referencing old_node's neighbors
Node1 {
val = 1
neighbors = [Node2, Node3]
}
hashmap= {'Node1':new_Node1, 'Node2': new_Node2}
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # BFS
        if not node:
            return

        def BFS(node):
            visited = set()
            queue = []
            # add node to the queue
            queue.insert(0,node)
            # update visited
            visited.add(node)
            while queue:
                node = queue.pop()

                # clone the node
                clone_node = Node()
                clone_node.val = node.val
                hashmap[node] = clone_node

                for nei in  node.neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        queue.insert(0,nei)

        hashmap = {}
        BFS(node)
        for key, val in hashmap.items():
            for nei in key.neighbors:
                c_node = hashmap[nei]
                val.neighbors.append(c_node)

        return hashmap[node]
