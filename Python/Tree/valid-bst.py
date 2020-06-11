# @Author: Sai Harshith
# @Date:   03-Feb-2020-16-02
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Difficulties faced: To write recursion logic
Time complexity: O(N)
Space complexity: O(N)
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower= float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val
            # main condition
            if val <= lower or val>=upper:
                return False

            # left node should be greater than - inf and less than its root
            if not helper(node.left, lower, val):
                return False

            # left node should be greater than its root and less than inf
            if not helper(node.right, val, upper):
                return False

            return True

        return helper(root)
