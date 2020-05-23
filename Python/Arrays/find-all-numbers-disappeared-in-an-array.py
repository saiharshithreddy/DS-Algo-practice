# @Author: Sai Harshith
# @Date:   2020-05-16T15:40:07-07:00
# @Last modified by:   Sai Harshith
# @Last modified time: 2020-05-22T13:01:12-07:00



class Solution:
    def findDisappearedNumbers(self, nums: List[int]):

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
