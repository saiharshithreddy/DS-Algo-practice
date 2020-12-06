'''
Approach 1: Two pointers
TC: O(n)
SC: O(1)

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1

        while left < right:
            # as the array is sorted
            if nums[left] + nums[right] == target:
                return True
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return False
