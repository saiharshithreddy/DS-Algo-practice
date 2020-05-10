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
        max_ones = max(max_ones, ones_subarray)
        return max_ones
        