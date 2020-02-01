# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        Approach 1: 
        TC:
        SC:
        '''
        ptr1, ptr2 = head, head
        count = 0

        while ptr1.next is not None:
            if count >= k:
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            count += 1
            ptr1 = ptr1.next

        ptr1.next = head
        ptr2.next = None