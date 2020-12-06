'''
Approach: Stack
Algo:
1. Create a min array with minimum values seen until that point in the array (nums). This list helps in determining the first element
in the 132 pattern. 
2. Consider elements with the property nums[j] > min[j] to be either pushed or popped based on below conditions. 
3. Create a monotonous decreasing stack and push when top element is greater than nums[j]
3. Pop from stack when top element is less than min[j] because our main idea is to get 1 from min[j] 3 from stack's top and 2 from nums[j] to form 132 pattern.
4. Make sure to remove invalid elements from the stack before pushing new elements. 

TC: O(N)
SC: O(N)
'''

class Solution:
    def find132pattern(self, nums: List[int]):
        
        min = float('inf')
        min_list = nums[:]
        
        # create a min array
        for i in range(len(nums)):

            if nums[i] < min:
                min = nums[i]
            # update with min value seen until now
            min_list[i] = min

        # monotonously decreasing stack 
        stack = []

        for j in range(len(nums)-1,-1,-1):
            if nums[j] > min_list[j]:

                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True

                stack.append(nums[j])          
        return False
                
            
            
                
                
                
            