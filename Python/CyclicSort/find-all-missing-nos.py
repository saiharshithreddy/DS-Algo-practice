'''
Approach: Cyclic sort
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N)
Space complexity: O(1) if result list is not considerd
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        # check if index + 1 = nums[index] and swap
        while i < n:
            j = nums[i]-1
            if  nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                i += 1

        missing_nums = []
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                missing_nums.append(i+1)

        return missing_nums
