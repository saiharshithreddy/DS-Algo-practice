class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        Triangle identity: Sum of two sides > third side
        Difference of two sides < third side

        Approach: Similar to 3 sum closest
        Left pointer at 0th index
        Right pointer at n-1th index

        Condition: nums[left] + nums[right] > nums[n] : As the array is sorted, left ++ still satisfies the condition so that why you add all the nums between left and right


        '''
        nums.sort() # O(NlogN)
        res = 0

        # O(N^2)
        for i in range(len(nums)-1, 1, -1):

            left, right = 0, i-1
            while left < right:

                if nums[left] + nums[right] > nums[i]:
                    res += (right - left)
                    right -= 1

                else:
                    left += 1
        return res

        
