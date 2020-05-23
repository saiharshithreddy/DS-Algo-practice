# @Author: Sai Harshith
# @Date:   22-May-2020-17-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-17-05


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        stack.append(root)
        # Preorder -> root, left, right
        while stack:
            root = stack.pop()
            if root:
                # Add root to result
                res.append(root.val)
                # right node is added to the stack first because stack.pop() will give us left node O(1)
                # In other way, we can add left first but then we have to do stack.pop(0) which is O(N)
                # also, going by the definition of a stack LIFO, pop() is correct usage.
                stack.append(root.right)
                stack.append(root.left)

        return res
