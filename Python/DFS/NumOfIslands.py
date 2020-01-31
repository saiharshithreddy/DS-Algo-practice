  
'''
Did it run on leetcode: Yes
Did you face any problem: None
Time Compelxity: 0(m*n)
Space Complexity: 0(m*n)
Algorithm:
- Convert the matrix into a flatten array
- Then add the first grid of the matrix into the queue
- Then add next 6 positions into the queue and increase the level
'''


class Solution:
    def numIslands(self, grid) -> int:
        
        # base case:
        if not grid:
            return 0
        count = 0

        for i in range(len(grid)):
            # traversing through a row
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i , j)
                    count += 1
        return count 

    def dfs(self, grid, i , j):
        # boundary condiitons
        if i < 0 or j < 0 or i >= len(grid) or j>= len(grid[0]) or grid[i][j] != '1':
            return
        # Visited node values are changed
        grid[i][j] = '#'
        # Move into 4 directions
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)