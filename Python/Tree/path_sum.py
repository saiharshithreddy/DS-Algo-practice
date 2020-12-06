# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Approach: Recursion
Difficulties faced: Could not write the recursive logic and terminating condition
Steps to resolve Difficulties:
Ran on Leetcode without help: Yes
Time complexity: O(N) visits every node in the tree
Space complexity: O(N) for recursive func ( call stack)
'''

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # base cases
        if root is None:
            return False

        # leaf node
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False

        # Has children
        if self.hasPathSum(root.left, sum - root.val):
            return True
        if self.hasPathSum(root.right, sum-root.val):
            return True
        return False
