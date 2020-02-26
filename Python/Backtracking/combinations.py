'''
Approach: Backtracking with DFS
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(kC(n,k))
Space complexity: O(C(n,k))

Algorithm:
1. DFS to generate all combinations.
2. Have to make sure that in a combination [i, j], i < j
'''
class Solution:
    def combine(self, n,k):
        res = []

        def dfs(curr, nums):
            if len(curr) == k:
                res.append(curr)
            # to avoid checking combinations of size greater than k
            elif len(curr) > k:
                return

            for i in range(len(nums)):
                dfs(curr + [nums[i]], nums[i+1:])
        dfs([],list(range(1,n+1)))
        # print(res)

if __name__ == '__main__':
    s = Solution()
    s.combine(4,2)
