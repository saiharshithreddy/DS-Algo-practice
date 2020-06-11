# @Author: Sai Harshith
# @Date:   18-May-2020-20-05
# @Last modified by:   Sai Harshith
# @Last modified time: 10-Jun-2020-15-06


'''
Approach 1: 2D DP matrix
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

'''
Approach 2: Dp array
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
