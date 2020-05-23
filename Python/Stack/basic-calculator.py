# @Author: Sai Harshith
# @Date:   12-May-2020-15-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-19-05


'''
"(1+(4+5+2)-3)+(6+8)"
1. '(' stack = [1,0]
2. 1 operand = 1
3. + res = 1 (sign) * 1 operand
4. '(' stack = [1,1,1,0]
5. 4 operand = 0 * 10 + 4 = 4
6. + res = 0 + 1 * 4 [res 4]
7. 5 operand = 5
8. + 4 + 1*5 = 9
9. 2 operand = 2
10 ) 9 * 1 and 9 + 1
'''
class Solution:
    def calculate(self, s: str) -> int:

        res = 0
        sign = 1
        operand = 0

        stack = []

        for ch in s:
            if ch.isdigit():
                operand =  (operand * 10) + int(ch)

            elif ch == '+' or ch == '*' or ch == '/':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0


            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif ch == ')':
                res += sign * operand

                res *= stack.pop() # sign

                res += stack.pop()

                operand = 0
        return res + (sign * operand)
