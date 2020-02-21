'''

Difficulties faced: Handling negative numbers and overflow
How did I resolve them:
Time complexity: O(logN)
Space complexity: O(1)

Algorithm:
'''
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = False
        if x < 0:
            sign = True
            x = abs(x)

        while x!= 0:
            rem = x % 10
            result = result * 10 + rem
            x = x//10

        # python doesn't have a limit. So manually check for overflow
        if result > 0x7FFFFFFF:
            return 0

        return result * -1 if sign else result
