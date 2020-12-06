'''
Approach: Using two stacks (Iteratively)
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N)
Space complexity: O(N)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []

        result = []
        if not root:
            return None

        # 1. add root to stack_a
        stack.append(root)
        while stack:
            # 2. Pop from stack_a and push to stack_b
            root = stack.pop()
            result.append(root.val)
            # 3. If children exist. Push into stack_a
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        # 4. Pop from stack_b
        return reversed(result)

        
