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
        if not root:
            return False

        if root.val > root.left.val or root.val < root.right.val:
            return False

         
        

        return self.isValidBST(root.left) and self.isValidBST(root.right)