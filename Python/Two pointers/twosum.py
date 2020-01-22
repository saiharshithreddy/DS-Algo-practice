'''
Approach 1: Using hash map, store new values in hash map, check if target - val is in hash map
TC: O(n)
SC: O(n) for hash map
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_indice = dict()
        for i, num in enumerate(nums):
            if target - num in val_to_indice:
                # if present return indices
                return [val_to_indice[target-num],i]
            else:
                val_to_indice[nums[i]] = i
        # if no such value
        return [-1,-1]