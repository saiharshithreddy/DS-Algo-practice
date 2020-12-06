'''
Similar to #130 Surrounded regions

Approach: 
1. Convert 0s to 1s on the borders because those islands are not surrounded by 1s on 4 sides. 
2. Count the DFS calls for islands  

TC: O(M*N)
SC: O(M*N)
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]):
    
        if not grid:
            return 0
        
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 0:
                return 
            grid[i][j] = 1
            for x,y in directions:
                dfs(grid, i+x, j+y)
        
        directions = [[0,1],[0,-1], [1,0], [-1,0]]
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                
                # dfs call on border elements
                if i==0 or j == 0 or i == row-1 or j == col - 1:
                    dfs(grid, i, j)
        
        closed_islands = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    dfs(grid, i, j)
                    closed_islands += 1
        return closed_islands