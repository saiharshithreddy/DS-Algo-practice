# @Author: Sai Harshith
# @Date:   01-Feb-2020-07-02
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS using queue
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)

        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentnode = queue.popleft()
                currentLevel.append(currentnode.val)

                if currentnode.left:
                    queue.append(currentnode.left)
                if currentnode.right:
                    queue.append(currentnode.right)


            result.append(currentLevel)
# ====================================================================
    # recursive
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []
        if not root:
            return levels

        def helper(node, level):
            if len(result) == level:
                result.append([])
            # add node value to the list
            result[level].append(node.val)
            # Recursive call the left and right childs
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return result
