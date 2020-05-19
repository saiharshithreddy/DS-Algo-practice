'''
Approach: Width is the difference between the right most node and left most node. 
At every level, we calculate the width and keep note of the maximum width. 
In a complete binary tree, left is at a position root*2 and right is at position root*2 + 1
Level order traversal. 
TC: O(N)
SC: O(N)
'''

class Solution:
    def widthOfBinaryTree(self, root: TreeNode):
        
        queue = collections.deque()
        queue.appendleft((root,0))
        width = 0
        
        while queue:
            level = []    
            size = len(queue)
            
            for _ in range(size):
                
                node, pos = queue.popleft()
                
                if node.left:
                    queue.append((node.left, pos*2))

                if node.right:
                    queue.append((node.right, pos*2+1))
                
                level.append([node.val,pos])
                
                # max of widths for every level. 
                width = max(width, level[-1][1] - level[0][1] + 1)
            
        return width