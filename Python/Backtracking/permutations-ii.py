'''
Approach:
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()

Algorithm:

'''
class Solution:
    def permuteUnique(self, nums):

        curr = []
        res = set()

        def dfs(curr, nums):
            if len(curr) == n and tuple(curr) not in res:
                res.add(tuple(curr))
            for i in range(len(nums)):
                dfs(curr + [nums[i]], nums[:i] + nums[i+1:])


        n = len(nums)
        dfs([], nums)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,1,2,3]))
