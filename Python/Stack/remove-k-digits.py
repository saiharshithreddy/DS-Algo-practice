# @Author: Sai Harshith
# @Date:   23-May-2020-10-05
# @Last modified by:   Sai Harshith
# @Last modified time: 23-May-2020-10-05

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        # monotonous increasing stack
        stack = []

        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])


        res = stack[:-k] if k else stack

        return ''.join(res).lstrip('0') or '0'
