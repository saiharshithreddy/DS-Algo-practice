# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack = []
        curr = root
        result = []
        while True:
            # reach the left most node
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            # pop the left most node and add it to the result
            # Move to the right node                
            elif stack:
                poped_item = stack.pop()
                result.append(poped_item.val)
                curr = poped_item.right 
            # stop when stack is empty and curr is None
            else:
                break
        return result
            
        
        