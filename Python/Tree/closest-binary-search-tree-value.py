# @Author: Sai Harshith
# @Date:   25-May-2020-12-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-12-05


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        def dfs(root):
            nonlocal smallest_diff, closest
            if not root:
                return 0

            if abs(root.val - target) < smallest_diff:
                smallest_diff = abs(root.val - target)
                closest = root.val
            dfs(root.left)
            dfs(root.right)

        smallest_diff = float('inf')
        closest = 0
        dfs(root)
        return closest
