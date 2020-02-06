# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Approach: DFS using iteration
Difficulties faced:
Steps to resolve Difficulties: 
Time complexity: O(H+k) H: height of the tree
Space complexity: O(H+k)
'''

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root.val) # add value
                root = root.left # move to left subtree
            root = stack.pop() # when reached leaf. Pop it
            k -= 1
            if k == 0: # check if K - no of nodes popped = 0
                return root.val
            root = root.right # move right
