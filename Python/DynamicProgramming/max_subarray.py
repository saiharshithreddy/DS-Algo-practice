'''
Attempt 1: Sliding window, could not store the window'sum after shrinking. 
Worked: Kadane's algorithm ( DP)
Time complexity: O(n)
Space complexity: O(1)
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # kadane's algorithm
        size = len(nums)
        max_sum = nums[0]
        
        for i in range(1,size):
            # adding a negative number will decrease the sum. to avoid that
            if nums[i-1]>0:
                # modify in-place
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)
            
        return max_sum