class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0,x)

    def pop(self) -> int:
        last = self.stack.pop(0)
        return last

    def top(self) -> int:
        return self.stack[0]

    def peekMax(self) -> int:
        return max(self.stack) if self.stack else 0

    def popMax(self) -> int:
        max_val = max(self.stack) if self.stack else 0
        self.stack.remove(max_val)
        return max_val



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
