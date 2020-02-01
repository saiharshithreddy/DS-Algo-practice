# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        Approach 1: Move one ptr first and then move both when first one moves k places forward 
        TC: O(n)
        SC: O(1)
        '''
        # base case
        if head is None:
            return 
        if head.next is None:
            return head
        # 1. Find the number of nodes
        ptr1, ptr2, temp = head, head, head
        count = 1
        while temp.next is not None:
            count += 1
            temp = temp.next 
        
        k = k % count
        count = 0
        # Update the links using pointers. First move one pointer k times and then move both together. 
        # Link the next variable of ptr1 to head and link next variable of ptr2 to None. 
        while ptr1.next is not None:
            if count == k:
                
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            else:
                count += 1
                ptr1 = ptr1.next
        
        ptr1.next = head
        new_head = ptr2.next
        ptr2.next = None
        
        return new_head