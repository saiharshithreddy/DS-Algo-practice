'''
Approach: Dynamic Programming
TC: O(N^2)
SC: O(N)



'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # dp array
        
        # [T,F,F,F,F,F,F,F,F] 
        dp = [0] * len(s)               # indicates True or False at that break position
        for i in range(len(s)):
            if s[:i + 1] in wordDict:   # current string till index i is directly found in dict, mark it TRUE
                dp[i] = 1
            else:
                for j in range(i):      # check if the current string can be TRUE, from breaking it (from index 0 to i)
                    if dp[j] and s[j + 1:i + 1] in wordDict:
                        dp[i] = 1
                        break
        return dp[-1]
            
            