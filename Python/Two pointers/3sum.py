class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # handling duplicates in 3sum
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two pointers approach    
            l, r = i+1, len(nums)-1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    # if equal to zero
                    res.append([nums[i], nums[l], nums[r]])
                    # to handle duplicates in 2sum
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res
        