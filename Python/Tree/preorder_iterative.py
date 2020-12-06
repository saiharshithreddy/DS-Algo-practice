# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        stack.append(root)
        
        while stack:
            root = stack.pop() 
            if root:
                res.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return res
                