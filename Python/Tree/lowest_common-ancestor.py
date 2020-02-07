# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print(root.val) if root else print(0)
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both left and right are p and q. return their parent as an ancestor
        if left and right:
            return root
        # if both left and right are not p and q
        elif left is None and right is None:
            return None
        # if only one leaf equals p or q propagate the the leaf above      
        if left and right is None:
            return left
        elif right and left is None:
            return right
