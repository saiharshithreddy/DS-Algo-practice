class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # range of the array is 1 to n
        # cyclic sort fails as there are duplicates
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] > 0:
                nums[j] = -nums[j]

        missing_nums = []

        for i in range(1,len(nums)+1):
            if nums[i-1] > 0:
                missing_nums.append(i)
        return missing_nums 
