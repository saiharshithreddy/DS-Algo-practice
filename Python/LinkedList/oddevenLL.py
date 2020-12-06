# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
        Approach 1:  
        TC: O(n)
        SC: O(1)
        '''
        # base case
        if head is None:
            return
          
        odd_head = head     # Initialize odd head
        even_head = head.next # initialize even head 
        temp = even_head
        while  odd_head.next is not None and temp.next is not None:
            odd_head.next = temp.next
            odd_head = odd_head.next
            temp.next = odd_head.next
            temp = temp.next
        # after odd nodes are linked and even nodes are linked. link the odd_head to even_head
        odd_head.next = even_head

        return head