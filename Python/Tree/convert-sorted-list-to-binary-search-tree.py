# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


'''
Similar to #108  Convert Sorted Array to Binary Search Tree 

Instead of an array it is linked list

Find middle element and recursive call on left of middle and right of middle 
Break the linked list into left, middle, right 
TC: O(N logN) (N/2 to find the middle, 2 N/4, 4 N/8 ....) (N/2 + 2 N/4 + 4 N/8...... = N/2 Log N) 
SC: O(H) or O(logN) bbecause only half tree is stored in a recursive stack
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        def middle(head):
            
            fast = head
            slow = head
            # to break the link between left list/right list and middle 
            prev = None
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next 
                
            # break link
            if prev:
                prev.next = None
            return slow
        
        if not head:
            return None
        
        mid = middle(head)

        root = TreeNode(mid.val)
        
        # if only one node
        if head == mid:
            return root
            
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
        