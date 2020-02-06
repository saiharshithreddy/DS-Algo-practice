# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # terminating condition
        elif root.left is None and root.right is None:
            return 1

        else:
            left_tree_height = self.maxDepth(root.left)
            right_tree_height = self.maxDepth(root.right)
            
            return max(left_tree_height, right_tree_height) + 1
