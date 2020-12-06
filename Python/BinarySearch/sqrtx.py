class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x


        low, high = 2, x//2

        while low <= high:
            mid = low + (high - low) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                high = mid - 1
            else:
                low = mid + 1
        return high


        
