# @Author: Sai Harshith
# @Date:   06-May-2020-16-05
# @Last modified by:   Sai Harshith
# @Last modified time: 22-May-2020-13-05


'''
Approach: Go over each num in the array and multiply -1 to the number at the index (num - 1)
and check if the number at that index is positive. If positive then that occured twice

TC: O(N)
SC: O(1)

'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate_nums = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1 # index

            nums[j] *= -1 # multiply -1

            if nums[j] > 0: # if positive then appears twice
                duplicate_nums.append(abs(nums[i]))
        return duplicate_nums
