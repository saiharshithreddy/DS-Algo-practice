class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        for index, ch in enumerate(s):
            if ch == '(':
                stack.append((ch,index))
                
                
            elif len(stack) != 0 and ch == ')' and stack[-1][0] == '(':
                stack.pop()
                             
            elif ch == ')':
                stack.append((ch, index))
                             
        print(stack)
        
        # stack contains unbalanced parenthesis so split the string excluding these parenthesis to make it valid
        res = s
        for para, index in stack:
            s = s[:index] + '$' + s[index+1:]
        
        return  s.replace('$','')
                