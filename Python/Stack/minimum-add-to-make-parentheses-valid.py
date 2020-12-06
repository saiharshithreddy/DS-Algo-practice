
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        stack = []
        for index, ch in enumerate(S):
            if ch == '(':
                stack.append((ch,index))
                
                
            elif len(stack) != 0 and ch == ')' and stack[-1][0] == '(':
                stack.pop()
                             
            elif ch == ')':
                stack.append((ch, index))
                
        return len(stack)
        
