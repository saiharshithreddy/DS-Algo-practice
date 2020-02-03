# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        '''
        Approach 1: Move first till nth node and
        then move both first and second till first reaches end 
        TC: O(n)
        SC: O(1)
        '''

        # base case
        if head.next is None:
            return 
        
        temp = ListNode(0)
        temp.next = head
        i = 0
        
        
        first = temp
        second = temp
        
        
        while first.next is not None:
            if i < n:
                first = first.next
                i += 1
            else:        
                second = second.next
                first = first.next
        # second will move till a node lesser than the node to be removed.
        # update the second's next with address of the next next node from second
        second.next = second.next.next
        
        return temp.next
                    