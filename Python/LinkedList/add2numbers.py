# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        current = ListNode(0)
        temp = current
        carry = 0
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            value = num1 + num2 + carry
            # when value > 9, only ten's digit is stored otherwise entire num
            current.next = ListNode(value%10)
            # Store the carry
            carry = value // 10

            # increment the linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next

        return temp.next
