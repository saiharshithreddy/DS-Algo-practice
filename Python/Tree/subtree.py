# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Approach: Recursion
Difficulties faced: Could not write recursive logic
Steps to resolve Difficulties: -
Time complexity: O(m*n)
Space complexity: O(n)
'''

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # terminating condition (all nodes in a subtree are visited)
        if not s: return False
        # check if both the root nodes are matched
        if self.isMatch(s,t):
             return True
        # now check with left subtree or right subtree
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isMatch(s,t):
        is not s and not t:
            return s is t
        # match the entire nodes in t with s
        return s.val == t.val: and self.isMatch(s.left, t.left) and self.isMatch(s.right, t.right)
