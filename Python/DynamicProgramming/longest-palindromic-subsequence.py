'''
Approach: Bottom up DP
Difficulties faced:
Steps to resolve Difficulties:
Time complexity: O(N^2)
Space complexity: O(N^2)

Algorithm:
1. Initialize a matrix with diagonal values as 1
2. Check if string[i] == string[j] as 
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # create a matrix
        dp = [[1 if i == j else 0 for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)-1,-1,-1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]

                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][len(s)-1]
