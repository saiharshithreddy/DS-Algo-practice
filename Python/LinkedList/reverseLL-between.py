# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
TC: O(n)
SC: O(1)
'''
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        current, previous = head, None
        count = 0
        
        # base case
        if m==n:
            return head
        # iterate till the start of the sublist
        while current is not None and count < m-1:
            previous = current
            current = current.next
            count += 1
        # store the node before the sublist 
        node_before_reverse = previous
        # store the first node of the sublist
        node_sublist = current
        count = 0
        # Reverse the sublist
        while current is not None and count < n-m + 1:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            count += 1
            
        # link the last node of the list before reversing the next nodes to the last node of the list to be reversed 
        if node_before_reverse is not None:
            node_before_reverse.next = previous
        else:
            head = previous
            
        node_sublist.next = current
        return head