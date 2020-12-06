# @Author: Sai Harshith
# @Date:   13-Jan-2020-22-01
# @Last modified by:   Sai Harshith
# @Last modified time: 26-May-2020-12-05



'''
Time complexity: O(n)
Space complexity: O(1) if output array is not considered as per the leetcode requirements. Otherwise O(n)
        left product right product approach
        without using additional space
        single pass O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]):


        left_product, right_product = 1, 1
        output = [0]*len(nums)
        # get the product  of elements on the left
        for i in range(1, len(nums)+1):
            output[i-1] = left_product
            # update leftproduct as move right
            left_product *= nums[i-1]

        # get the product of elements on the right
        for j in range(len(nums)-1,-1,-1):

            output[j] *= right_product
            # update rightproduct as you move left
            right_product *= nums[j]

        return output
