# @Author: Sai Harshith
# @Date:   22-May-2020-18-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-18-05

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        # find max

        def find_max(nums):
            max_ = float("-inf")
            index = 0
            for i in range(len(nums)):
                if nums[i] > max_:
                    max_, index = nums[i], i
            return max_, index
)
        def construct_tree(nums):
            if len(nums) == 0:
                return None

            val, index = find_max(nums)
            root = TreeNode(val)
            root.left = construct_tree(nums[:index])
            root.right = construct_tree(nums[index+1:])
            return root


        root = construct_tree(nums)
        return root
