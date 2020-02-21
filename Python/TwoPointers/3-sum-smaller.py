'''
Approach 1: Two pointers without removing duplicate triplets
TC: O(n^2)
SC: O(1)
'''

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
         
        nums.sort() 
        count_of_triplets = 0   
        for i in range(len(nums)-2):

            left, right = i+1, len(nums)-1

            while left < right:

                if nums[i] + nums[left] + nums[right] < target:
                    # right - left because after sorting if i,left,right < target i,left, right-1 and so on sum is less  than target
                    count_of_triplets += right - left
                    
                    left += 1
                else:
                    right -= 1
                   
        return count_of_triplets





'''

Approach 1: Two pointers By removing duplicate triplets
TC: O(n^2)
SC: O(1)
'''

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        '''
        num1 + num2+ num3 < target
        Return: No of triplets 
        ''' 
        nums.sort() 
        count_of_triplets = 0   
        for i in range(len(nums)-2):

            # To avoid duplicates in 3 sum
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1

            while left < right:
                        
                if nums[i] + nums[left] + nums[right] >= target:
                    right -= 1

                elif nums[i] + nums[left] + nums[right] < target:
                    # right - left because after sorting if i,left,right < target i,left, right-1 and so on sum is less  than target
                    count_of_triplets += right - left
                    # To avoid duplicates in 2 sum
                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                    left += 1
                   
        return count_of_triplets
