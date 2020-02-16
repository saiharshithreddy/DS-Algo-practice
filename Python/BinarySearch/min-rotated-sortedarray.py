'''
Approach: 1. Single pass O(N) 2. BinarySearch
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(logN)
Space complexity: O(1)

Algorithm:
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #minimum = float('inf')
        # O(N)
#         for i in range(len(nums)):
#             if nums[i] < minimum:
#                 minimum = nums[i]

#         return minimum

        # O(logN) BinarySearch
        #base case
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return 1

        low = 0
        high = len(nums)-1

        # sorted array
        if nums[high] > nums[0]:
            return nums[0]

        while low <= high:
            mid = low + (high - low)//2
            # 1. when mid is rotated index
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            # 2. as elements are in sorted array before rotating, the vals are generally 
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            # 3.when mid > low then the lowest val is on the right
            if nums[mid] > nums[low]:
                low = mid + 1

            else:
                high = mid - 1
