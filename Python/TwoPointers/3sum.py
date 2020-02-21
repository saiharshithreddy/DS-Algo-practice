'''
Approach 1:
TC: O(n2)
SC: O(k) // Result array
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()                                             # 1. Sort
        for i in range(len(nums)-2):
                                                                #2. handling duplicates in 3sum
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two pointers approach    
            l, r = i+1, len(nums)-1
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                
                if sum < 0:
                    l +=1 
                elif sum > 0:
                    r -= 1
                else:
                    # if equal to zero
                    res.append([nums[i], nums[l], nums[r]])
                                                                #3. Handling duplicates in 2sum

                    # if two consecutive same nums, increment left twice
                    # and likewise right if  two consecutive nums from the right
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
        