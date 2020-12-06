'''
Approach 1: Two pointers
TC: O(n)
SC: O(1)
'''

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        left, right = 0, 1
        nums.sort()
        pair_count = 0
        while right < len(nums):
            if nums[right] - nums[left] == k:
                pair_count += 1
                left += 1
                right += 1
                while nums[left] == nums[left-1] and nums[right] == nums[right-1]:
                    left += 1
                    right += 1
            elif nums[right] - nums[left] < k:
                right += 1
            else:
                break
            
        return pair_count
