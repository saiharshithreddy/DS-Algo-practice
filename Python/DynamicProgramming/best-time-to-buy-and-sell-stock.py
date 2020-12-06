class Solution:
    def maxProfit(self, prices) -> int:

        profit = 0
        buy_price = float('inf') # we want buy price to be min so intialize it with max
        
        for i in range(len(prices)):
            # update buy price if buy price on ith day is less than the previous min buying price.
            if prices[i] < buy_price:
                buy_price = prices[i]
            # profit = selling price - buying price
            # on days after stock is bought you can sell. check for profit on each upcoming day you want to sell. 
            elif profit < prices[i] - buy_price:
                profit = prices[i] - buy_price
            
        return profit
        

        