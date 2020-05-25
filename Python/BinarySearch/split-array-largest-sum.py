# @Author: Sai Harshith
# @Date:   25-May-2020-03-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-03-05

'''
Similar to # capacity to ship packages
Binary Search
TC: O(NlogN)

'''

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        # O(logN)
        while left <= right:
            mid = (left + right) // 2
            count = 1
            max_sum = 0
            # O(N)
            for n in nums:
                if max_sum + n > mid:
                    max_sum = 0
                    count += 1
                max_sum += n

            if count > m:
                left = mid + 1
            else:
                right = mid - 1
        return left
