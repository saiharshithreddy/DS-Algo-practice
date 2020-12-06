# @Author: Sai Harshith
# @Date:   01-Feb-2020-07-02
# @Last modified by:   Sai Harshith
# @Last modified time: 11-Jun-2020-00-06

'''
Approach: BFS

Time complexity: O(N)
Space complexity: O(N) for deque

Algorithm:
1. Find the average by doing a level order traversal 
'''

from collections import deque
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # bfs
        queue = deque()
        res = []
        queue.appendleft(root)

        while queue:
            levelSize = len(queue)

            level_sum = 0
            for _ in range(levelSize):
                node = queue.popleft()
                # sum for each level
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # average of each level
            res.append(level_sum / len(levelSize))

        return res
