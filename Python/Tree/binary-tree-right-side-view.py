# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Approach: Level order traversal
Difficulties faced: DFS approach
Steps to resolve Difficulties:
Time complexity: O(N)
Space complexity: O(N)

Algorithm: Level order traversal
1. Retrieve the last element from each level
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        res = []
        def helper(root, level):
            if len(res) == level:
                res.append([])

            res[level].append(root.val)
            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, 0)
        return [x[-1] for x in res]
