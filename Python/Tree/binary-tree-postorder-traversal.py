# @Author: Sai Harshith
# @Date:   22-May-2020-17-05
# @Last modified by:   Sai Harshith
# @Last modified time: 07-Jun-2020-23-06


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

            # 2. Pop from stack_a and push to result
            root = stack.pop()
            result.append(root.val)

            # 3. If children exist. Push into stack_a
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return reversed(result)
