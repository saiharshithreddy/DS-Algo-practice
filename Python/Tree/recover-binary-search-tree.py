# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        
        def dfs(node):
            
            # inorder
            if not node:
                return 
            
            dfs(node.left)
            if self.prev_node:
                if self.prev_node.val > node.val:
                    if self.first == None:
                        self.first = self.prev_node
                    self.last = node
            self.prev_node = node
            dfs(node.right)
            
            
        self.first = None
        self.last = None
        self.prev_node = None
        dfs(root)
        
        # swap 
        self.first.val, self.last.val = self.last.val, self.first.val