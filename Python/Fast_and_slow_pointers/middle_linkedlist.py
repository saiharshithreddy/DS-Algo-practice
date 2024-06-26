# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            
            slow = slow.next
            fast = fast.next.next
            
        return slow
        