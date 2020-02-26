'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()

Algorithm:

'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        curr = []
        res = set()

        def dfs(curr, nums):
            if len(curr) == n and tuple(curr) not in res:
                res.add(tuple(curr))
            for i in range(len(nums)):
                dfs(curr + [nums[i]], nums[:i] + nums[i+1:])


        n = len(nums)
        dfs([], nums,n)
        return res
