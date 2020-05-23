# @Author: Sai Harshith
# @Date:   22-May-2020-17-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-17-05



class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # left, root, right
        stack = []
        curr = root
        result = []
        while stack or curr:
            # root to left are appended to the stack
            if curr:
                stack.append(curr)
                curr = curr.left

            elif stack:
                poped_item = stack.pop()
                result.append(poped_item.val)
                curr = poped_item.right

        return result
