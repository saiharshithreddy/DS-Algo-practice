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
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum / len(levelSize))

        return res
