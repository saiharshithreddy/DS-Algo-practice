'''
Approach: Modified binary search
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(logN)
Space complexity: O(1)
'''

class Solution:
    def searchRange(self, nums, target):

        result = []

        first_pos = self.binarysearch(nums, target, True)
        
        if first_pos == len(nums) or nums[first_pos] != target:
            return [-1,-1]


        last_pos = self.binarysearch(nums, target, False )


        return [first_pos, last_pos-1]


        # modified binary search
    def binarysearch(self, nums,val, left):
        low = 0
        high = len(nums)
        while low <= high:

            mid = (low + high )//2

            if nums[mid] > val or (left and nums[mid] == val):
                high = mid - 1
            else:
                low = mid + 1

        return low

if __name__ == '__main__':
    s= Solution()
    res = s.searchRange([1,2,3,4,4,5],4)
    print(res)

