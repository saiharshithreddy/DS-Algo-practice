# @Author: Sai Harshith
# @Date:   25-May-2020-12-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-12-05

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_val):
            if not node:
                return

            if node.val >= max_val:
                self.count += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        self.count = 0
        max_val = root.val
        dfs(root, max_val)
        return self.count
        
