# @Author: Sai Harshith
# @Date:   24-May-2020-21-05
# @Last modified by:   Sai Harshith
# @Last modified time: 25-May-2020-11-05

class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0]* (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            for j in range(i):
                # left subtree * right subtree
                dp[i] += dp[j] * dp[i-j-1]

        return dp[-1]
