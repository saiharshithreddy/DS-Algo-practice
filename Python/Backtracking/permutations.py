# @Author: Sai Harshith
# @Date:   26-Feb-2020-01-02
# @Last modified by:   Sai Harshith
# @Last modified time: 27-May-2020-11-05



'''
Approach: Backtracking with dfs
Time complexity: O(N*N!)
Space complexity: O(N*N!)

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
