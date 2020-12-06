class Solution:
    def numSquares(self, n: int) -> int:
        
        sq_nums = [x**2 for x in range(1, int(math.sqrt(n))+1)]
        
        # create a dp array 
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            for square in sq_nums:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]
                
        
        
        