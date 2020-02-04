# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Approach: 
Difficulties faced: To get the intuition of writing a recursive logic
Time complexity: O(N)
Space complexity: O(N)

'''

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_depth = 0

        def depth( root):

            # base case
            if root is None: return 0
            
            # left subtree
            left = depth(root.left)
            # right subtree
            right = depth(root.right)

            self.max_depth = max(self.max_depth, left + right)
            
            return max(left, right) + 1
        
        depth(root)

        return self.max_depth