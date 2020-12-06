# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # fast and slow pointer
        
        fast, slow = head, head
        # loop until the fast pointer reaches the last node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
        