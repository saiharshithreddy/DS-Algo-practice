class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])
    
        for i in range(1, row):
            for j in range(col):
                if j > 0 and j < col-1:
                    A[i][j] += min(A[i-1][j], A[i-1][j-1], A[i-1][j+1]) 
                elif j == 0:
                    A[i][j] += min(A[i-1][j],  A[i-1][j+1]) 
                else:
                    A[i][j] += min(A[i-1][j],  A[i-1][j-1])
        
        return min(A[-1])