'''
Approach: Two pointers
TC: O(n^3)
SC: O(n) for quadraplets array
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #1. Sort the array
        nums.sort() # O(nlogn)
        quadraplets = []

        for i in range(len(nums)-3):
            # handling duplicates in 4sum
            if i>0 and nums[i] == nums[i-1]:
                continue
            # 3 sum
            for j in range(i+1, len(nums)-2):
                # handling duplicates in 3 sum
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                self.search_pairs(nums, target, i, j, quadraplets)

    def search_pairs(self, nums, target, i, j, quadraplets):
        left =  j+1
        right = len(nums)-1

        while left < right:
            sum = nums[i] + nums[j] + nums[left] + nums[right]
            if sum == target:
                quadraplets.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -=1
                # handling duplicates in 2 sum 
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1



