'''
Approach 1: two pointers
TC: O(n)
SC: O(1)
'''

import math
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        # find the first number out of sorting order
        while low < len(nums) - 1 and nums[low] <= nums[low+1]:
            low += 1
        # if array is sorted    
        if low == len(nums) - 1:
            return 0
        
        # find the last number out of sorting order
        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1
            
        
        # find the max and min of subarray
        subarray_min = math.inf
        subarray_max = -math.inf
        
        for i in range(low, high+1):
            subarray_max = max(subarray_max, nums[i])
            subarray_min = min(subarray_min, nums[i])
            
        while low > 0 and nums[low-1] > subarray_min:
            low -= 1
            
        while high < len(nums)-1 and nums[high+1] < subarray_max:
            high += 1
            
        return high - low + 1
            
        
        
        