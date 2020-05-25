# @Author: Sai Harshith
# @Date:   25-May-2020-12-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-12-05
'''
Similar to # find-the-smallest-divisor-given-a-threshold

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2
            eating_speed = 0
            k = 0
            for p in piles:
                eating_speed += math.ceil(p/mid)

            if eating_speed > H:
                left = mid + 1
            else:
                right = mid -1
        return left 
