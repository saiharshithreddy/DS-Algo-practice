'''
Approach: Cyclic sort
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N)
Space complexity: O(1)
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        i = 0
        n = len(nums)
        # cyclic sort.
        while i< n:
            j = nums[i]-1
            # cyclic sort applies to 1<= x <= n so check the number is in that range 
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
                #swap
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # check if val equals index + 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        # if the array contains all positive integers then return the next positive integer
        return len(nums) + 1
