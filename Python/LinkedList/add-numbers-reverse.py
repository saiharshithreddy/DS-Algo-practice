# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        current = ListNode(0)
        i,j = 0,0
        # loop till the last node in the lists
        while l1.next is not None or l2.next is not None:
            if l1.next is not None:
                l1 = l1.next
                i += 1
            if l2.next is not None:
                l2 = l2.next
                j += 1
        l1_size = i+1
        l2_size = j+1
        m,n=0,0
        carry = 0
        # Add the nodes 
        while m < l1_size or n < l2_size:

            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            value = num1 + num2 + carry
            carry = value // 10
            node = ListNode(value%10)
            last = node
            
                
        
        