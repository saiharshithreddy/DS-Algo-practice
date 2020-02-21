'''
Approach 1: Two pointers
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Dutch national flag problem
        
        # O(n) and O(1)
        smaller, equal, larger = 0,0,len(nums)
        while equal < larger:
            if nums[equal] == 0:
                # swap
                nums[smaller] , nums[equal] = nums[equal], nums[smaller]
                smaller += 1
                equal += 1
            elif nums[equal] == 1:
                equal += 1
            else:
                larger -= 1
                # swap
                nums[equal], nums[larger] = nums[larger], nums[equal]
        
        