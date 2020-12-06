# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Approach: Recursion
Difficulties faced: To handle cases when only one child. I returned min(left_depth, right_depth)+1 but when there is only
child the min(left_depth, right_depth) will become 0 (Wrong)
Steps to resolve Difficulties:  Initialize min_depth variable to inf and check for min(left, min_depth) or min(right, min_depth)
Ran on Leetcode without help:  No
Time complexity: O(N)
Space complexity: O(logN)
'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        # terminating condition
        if root is None:
            return 0

        min_depth = float('inf')
        # if no children
        if not root.left and not root.right:
            return 1
        # only left
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        # only right
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1
