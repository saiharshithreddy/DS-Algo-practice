'''
Time complexity: O(n)
Space complexity: O(1) if output array is not considered as per the leetcode requirements. Otherwise O(n)

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left product right product approach
        # without using additional space
        # single pass O(n)
        
        left_product, right_product = 1, 1
        output = [0]*len(nums)
        # get the product  of elements on the left 
        for i in range(1, len(nums)+1):
            output[i-1] = left_product
            # update leftproduct as move right
            left_product *= nums[i-1]
            
        # get the product of elements on the right    
        for j in range(len(nums)-1,-1,-1):
            
            output[j] = output[j] * right_product
            # update rightproduct as you move left
            right_product *= nums[j]
        
        return output
            
            
            
        