'''
Approach: Modified binarysearch
Difficulties faced: Could not come with a modified BinarySearch logic
Steps to resolve Difficulties:
Time complexity: O(logN )
Space complexity: O(1)
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = low + (high-low) //2
            halvesareEven = True if high - mid % 2 == 0 else False

            if nums[mid] == nums[mid+1]:                # 1. When num at mid and mid + 1 index are equal.
                if halvesareEven:
                    low = mid + 2
                else:
                    high = mid - 1

            elif nums[mid] == nums[mid-1]:             #2. When
                if halvesareEven:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]

        return nums[low]
