'''
Time complexity: O(1)
Space complexity: O(capacity)
'''


# doubly linkedlist
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        # head and tail
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        n = self.map[key]
        # Move the node first of the list 
        self.remove(n)
        self.add_front(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        # update the value for the key
        n = Node(key,value)
        self.add_front(n)
        self.map[key] = n
        if len(self.map) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.map[n.key]
            
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def add_front(self,node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)