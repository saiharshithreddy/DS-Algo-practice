# @Author: Sai Harshith
# @Date:   08-May-2020-20-05
# @Last modified by:   Sai Harshith
# @Last modified time: 26-May-2020-12-05

'''
TC: O(N)
SC: O(1)

'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_ones = 0
        ones_subarray = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones_subarray += 1
            else:
                max_ones = max(max_ones, ones_subarray)
                ones_subarray = 0

        # to calculate max ones in a subarray which is the last subarray ex: 1000111, 111 is a subarray with ones 3
        max_ones = max(max_ones, ones_subarray)
        return max_ones
