class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer approach
        # return the size of the array without duplicates
        non_dup = 1 
        for i in range(1,len(nums),1):              #1. Loop over the array starting from 1     
            
            if nums[non_dup - 1] != nums[i]:          #2. Check if num is not equal to prev num 
                nums[non_dup] = nums[i]               # Increment non_dup (unique nums)      
                non_dup += 1
            
        return non_dup
                
        