"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        iterator = head
        hashmap = {}
        while iterator:
            node = Node(0)
            node.val = iterator.val
            hashmap[iterator] = node

            iterator = iterator.next
        # print(hashmap)
        for k, v in hashmap.items():
            next_node = k.next
            random_ptr = k.random

            dup_next = hashmap[next_node] if next_node else None
            random_ptr = hashmap[random_ptr] if random_ptr else None
            v.next = dup_next
            v.random = random_ptr
        nodes = list(hashmap.values())
        # print(nodes[0].val)
        return nodes[0]

            
