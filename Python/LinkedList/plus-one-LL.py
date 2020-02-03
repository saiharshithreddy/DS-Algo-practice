# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy
        
        while head:
            if head.val != 9:
                not_nine = head

            head = head.next
        # increment not nine by 1
        not_nine.val = not_nine.val + 1
        # nodes after are all 9s
        nine = not_nine.next

        # change 9s to 0
        while nine:
            nine.val = 0
            nine = nine.next
        # if all nodes are 9s return dummy otherwise dummy.next    
        return dummy if dummy.val else dummy.next