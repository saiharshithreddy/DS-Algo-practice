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
        
