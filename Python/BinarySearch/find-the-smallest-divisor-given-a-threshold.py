# @Author: Sai Harshith
# @Date:   25-May-2020-04-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-04-05

'''
Binary Search
If the sum > threshold, the divisor is too small.
If the sum <= threshold, the divisor is big enough.

Time O(NlogK), where K = max(A)
Space O(1)
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left, right = 1, max(nums)


        while left <= right:
            mid = (left + right) // 2

            max_sum = 0
            for num in nums:
                max_sum += math.ceil(num/mid)
            if max_sum > threshold:
                left = mid + 1
            else:
                right= mid - 1
        return left

        
