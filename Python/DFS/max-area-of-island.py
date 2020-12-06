'''
Approach: Same as number of islands
Count the number of dfs calls inside a dfs call. 
TC: O(R*C)
SC: O(1)
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, i,j):
            
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return
            
            self.count += 1
            grid[i][j] = '#'
            
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
            
            return self.count 
        self.count = 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = dfs(grid, i, j)
                    max_area = max(max_area, count)
                    # reset for every dfs call
                    self.count = 0
        return max_area