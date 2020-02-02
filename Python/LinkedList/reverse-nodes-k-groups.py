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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # base case
        if k<= 1 or head is None:
            return head
        
        current, previous = head, None

        # Similar to reverse a sublist but have to do it for multiple sublists. Infinite loop and break it
        # when it reaches end.  
        while True:
            node_before = previous
            lastnode_sublist = current

            i = 0
            # reverse 
            while current is not None and i<k:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
                i += 1
            # link the node before reverse to the last node of the reversed sublist.
            if node_before is not None:
                node_before.next = previous
            else:
                head = previous
            # node before reversal should point to the start of the next sublist. 
            lastnode_sublist.next = current

            # breaking the loop condiition
            if current is None:
                break
            # update the previous as the last reversed node. 
            previous = lastnode_sublist
            # Continue the same for next sublist.

        return head
        