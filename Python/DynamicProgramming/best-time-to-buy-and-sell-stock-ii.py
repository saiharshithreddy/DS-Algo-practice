'''
Approach: Peak and Valley idea

There will be profit if price on day i > price on day i-1 
Add all (peak - valley) for max profit. 
TC: O(N)
SC: O(1)

'''
class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        
        for i in range(1,len(prices)):
            # peak - valley
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
                
        return max_profit
            


