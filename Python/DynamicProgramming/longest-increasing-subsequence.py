'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N^2)
Space complexity: O(N)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # longest increasing subsequence
        LIS = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                
                if nums[i] > nums[j] and LIS[i] <= LIS[j]:
                    LIS[i] = LIS[j] + 1


        return max(LIS)
