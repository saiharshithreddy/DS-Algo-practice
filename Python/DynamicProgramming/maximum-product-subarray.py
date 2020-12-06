class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_max = currmin = currmax = nums[0]
        
        # Consider: Negative * Negative = positive
        for num in nums[1:]:
            currmax, currmin = max(currmin * num, currmax * num, num), min(currmin * num, currmax *  num, num)
             
            
            largest_max = max(largest_max, currmax)
        return largest_max
            

        