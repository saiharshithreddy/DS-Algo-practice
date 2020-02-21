from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Sliding window O(n)
        
        # base case 
        if k<=1: return 0
        
        window_start, count = 0,0
        product = 1
        
        for window_end in range(len(nums)):
            right_num = nums[window_end]
            product *= right_num 
            
        
            while product >= k:
                # remove the left num val from the product
                product /= nums[window_start]
                # Shrink the window
                window_start += 1
                
            # num of pairs satisfying the condition    
            count += window_end - window_start + 1
        
        return count
                