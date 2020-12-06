class Solution:
    def minPathSum(self, grid: List[List[int]]):
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                # first row numbers can be reached by moving right only.
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                # first col numbers can be reached by moving down only.
                if j == 0 and i > 0:
                    grid[i][j] += grid[i-1][j]
                # check the min of way to reach this position either by moving right or down 
                elif i >0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        print(grid)
        return grid[-1][-1]
                    
        