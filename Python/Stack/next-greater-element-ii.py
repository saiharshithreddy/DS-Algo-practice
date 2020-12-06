'''
As it is a circular array we need to iterate from the start once we are over the array. meaning two times.
TC: O(N)
SC: O(N)

'''
class Solution:
    def nextGreaterElements(self, nums):
        if len(nums) == 0:
            return []
        stack = []
        res = [-1] * len(nums) # default values
        
        # twice the length of nums with values [0...n, 0,...n]
        for i in list(range(len(nums))) * 2: 
            # monotonous decreasing stack concept
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
            
        return res
        