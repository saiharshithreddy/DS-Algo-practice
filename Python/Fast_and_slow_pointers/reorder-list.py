# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Approach 1: Find middle and reverse the second half. Merge them one by one. 
        TC: O(n)
        SC: O(1)
        """
        middle_node = self.middle(head)
        second_head = self.reverse(middle_node)
        new_head = self.mergelist(head, second_head)
        

    def middle(self, head):
        if head is None or head.next is None:
            return 
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next # move the next node
            current.next = prev # reverse the link
            prev = current # move prev to current
            current = next_node # move current to next

        return prev

    def mergelist(self, first_head, second_head):
        
        start_node = first_head
        while first_head is not None and second_head is not None:
            # store the next node's location to assign it to the second half's head
            next_node_1 = first_head.next
            first_head.next = second_head
            # store the next node's location to assign it to the first half's head
            next_node_2 = second_head.next
            second_head.next = next_node_1
            # move the heads of the two halves. 
            first_head = next_node_1
            second_head = next_node_2
            
        # when we encounter a node which is the last node of the first half of the list. Point it to None 
        if first_head is not None:
            first_head.next = None
        return start_node

    


        