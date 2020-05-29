# @Author: Sai Harshith
# @Date:   10-Jan-2020-12-01
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-15-05



'''
Fast look ups and fast removals.
Idea: Hashmap and doubly linked list.

TC: O(1)
SC: O(capacity)
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

        # Once the node is accessed it has to be moved to front.
        n = self.map[key]
        # 1. Remove from its position
        self.remove(n)
        # 2. Add in front
        self.add_front(n)
        return n.value

    def put(self, key: int, value: int) -> None:
        # put also works as update.
        if key in self.map:
            self.remove(self.map[key])
        # update the value for the key
        n = Node(key,value)
        self.add_front(n)
        self.map[key] = n
        # check for capacity and remove node in the end.
        if len(self.map) > self.capacity:
            n = self.tail.prev
            self.remove(n)
            del self.map[n.key]

    def remove(self, node):
        # standard doubly linkedlist deletion
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add_front(self,node):

        # 1. node's prev should point to head
        node.prev = self.head
        # 2. new node should point to prev start node
        node.next = self.head.next
        # 3. head.next.prev should point to node
        self.head.next.prev = node
        # 4. head's next should point to node
        self.head.next = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
