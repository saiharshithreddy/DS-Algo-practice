class Solution:
    def reverseKgroupsAlternatively(self, head: ListNode, k: int) -> ListNode:
        if k <= 1 or head is None:
            return head

        previous, current = None, head
        i = 0
        while True:
            node_before = previous
            last_node_sublist = current

            while current is not None and i < k:
                next_node = current.next 
                current.next = previous
                previous = current
                current = next_node
                i += 1

            if node_before:
                node_before.next = previous

            # if there is no node before 
            else:
                head = previous
            
            last_node_sublist.next = current
            
            # skip k nodes 
            while current is not None and i< k:
                previous = current
                current = current.next 
                i += 1

            if current is None:
                break
        return head