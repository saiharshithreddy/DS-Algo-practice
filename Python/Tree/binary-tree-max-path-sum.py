# @Author: Sai Harshith
# @Date:   11-Apr-2020-04-04
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def max_pathSum(root):
            if not root:
                return 0

            left_sum = max(max_pathSum(root.left),0)
            right_sum = max(max_pathSum(root.right),0)

            pathSum = root.val + left_sum + right_sum
            self.max_sum = max(self.max_sum, pathSum)
            return root.val + max(left_sum ,right_sum)

        self.max_sum = float('-inf')
        max_pathSum(root)
        return self.max_sum
