# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []

        # create a graph
        def create_graph(root):
            if not root:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)

            create_graph(root.left)
            create_graph(root.right)

        graph = defaultdict(list)
        create_graph(root)

        # check for nodes k distance from target by doing DFS
        def dfs_graph(node, dist):
            visited.add(node)
            if dist == 0:
                res.append(node)
                return
            for nei in graph[node]:
                if nei not in visited:
                    dfs_graph(nei, dist-1)

        visited = set()
        res = []
        dfs_graph(target.val,K)
        return res
  
# ========================================================
'''
 Solution - Approach 2
'''

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        ans = []
        def dfs(root):
            if root is None:
                return -1
            # target is found so return 1
            elif root is target:
                find_nodes(root, 0)
                return 1
            
            else:
                l =dfs(root.left)
                r = dfs(root.right)

                if l != -1:
                    if l == K:
                        ans.append(root.val)
                    # find_nodes since distance is <= k
                    if l <= K:
                        find_nodes(root.right, l+1)
                    return l+1
                elif r != -1:
                    if r == K:
                        ans.append(root.val)
                    # find_nodes since distance is <= k
                    if r <= K:
                        find_nodes(root.left, r+1)
                    return r+1
                else:
                    return -1


        # Calculation of k distance neighbours
        def find_nodes(root, distance):
            if root is None or distance > K:
                return
            if distance == K:
                ans.append(root.val)
                return
            else:
                find_nodes(root.left, distance+1)
                find_nodes(root.right, distance+1)
        dfs(root)
        return ans      
