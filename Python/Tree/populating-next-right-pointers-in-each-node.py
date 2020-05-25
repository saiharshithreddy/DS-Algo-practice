# @Author: Sai Harshith
# @Date:   24-May-2020-19-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-19-05

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None
        cur  = root
        next_node = root.left

        while cur.left :
            # left node has to point to right
            cur.left.next = cur.right
            # changing the pointers by level.

            if cur.next:

                cur.right.next = cur.next.left
                cur = cur.next
            
            else:
                cur = next_node
                next_node = cur.left

        return root
