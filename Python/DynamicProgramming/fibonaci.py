class Solution:
    memo = []
    def fib(self, N: int) -> int:
        if N<2:
            return N
        memo = [0]*(N+1)
        memo[0] = 0
        memo[1] = 1
        for k in range(2, N+1):
            memo[k] = memo[k-1] + memo[k-2]
        return memo[N]
            
