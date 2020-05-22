# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode):
        if not root:
            return
        # if a node's x co-ord matches then they are on the same vertical line

        # bfs

        graph = collections.defaultdict(list)

        queue = collections.deque()
        queue.appendleft((0,root))
        level = 0
        left = float('inf')
        right = float('-inf')
        while queue:
            
            for _ in range(len(queue)):
                pos, node = queue.popleft()
                if pos < left: left = pos
                if pos > right: right = pos
                graph[pos].append((level, node.val))
                
                if node.left:
                    queue.append((pos - 1, node.left))
                if node.right:
                    queue.append((pos + 1, node.right))
            level += 1

        res = []
        for i in range(left, right+1):
            res.append([n[1] for n in (sorted(graph[i]))])
        return res
        
        

        
        
        
        
        
            
        