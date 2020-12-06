'''
Approach 1:  
TC:
SC:
'''


import math
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # O(nlogn)
        res = nums[0] + nums[1] + nums[2]                       # 1. initialize the result
        for i in range(len(nums)):
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == target:                                # 2. If sum of 3 nums equals target return the sum
                    return s
                
                if abs(s-target) < abs(res - target):          # 3. check the difference
                    res = s
                
                if s < target:                                  # 4. Increment left pointer
                    left += 1
                elif s > target:                                # 5. Decrement right pointer
                    right -= 1
                
                
        return res             
        