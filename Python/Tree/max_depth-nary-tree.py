"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
Approach: DFS with Recursion
Difficulties faced: None
Steps to resolve Difficulties:
Time complexity: O(H) H: height of the tree
Space complexity: O(H)
'''

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        # base case
        if root is None:
            return 0

        # only root node
        elif root.children == []:
            return 1

        # has children
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1
