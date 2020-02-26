'''
Approach: Backtracking with dfs
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O()
Space complexity: O()

Algorithm:

'''
class Solution:
    def permute(self, nums):
        res = []
        n = len(nums)
        def dfs(curr, nums):
            if len(curr) == n:
                res.append(curr)
            for i in range(len(nums)):
                dfs(curr + [nums[i]], nums[:i]+nums[i+1:])


        dfs([], nums)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
