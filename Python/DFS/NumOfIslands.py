# @Author: Sai Harshith
# @Date:   31-Dec-2019-06-12
# @Last modified by:   Sai Harshith
# @Last modified time: 08-Jun-2020-20-06



'''
Approach: DFS 
Time complexity : O(MN) where M is the number of rows and N is the number of columns.

Space complexity : worst case O(M N) in case that the grid map is filled with lands where DFS goes by M×N deep
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i,j):
            # out of bounds and when there is no land - func return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            # change the value to any str so you dont go into recursive loop / visited idea can also be used 
            # -- Two ways to keep track of a cell(i,j) which is traversed.
            grid[i][j] = '#'
            # visited.add((i,j))
            
            # move in 4 directions
            for x,y in move(i,j):
                dfs(grid, x, y)

          
        def move(i,j):
            directions  = [[0,1],[1,0],[-1,0],[0,-1]]
            for x,y in directions:
                if 0 <= i + x < row or 0 <= j + y < col:
                    yield i + x, j + y
        
        row = len(grid)
        col = len(grid[0])
#         visited = set()
        # One dfs call will give you one island 
        island_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(grid, i , j)
                    island_count += 1
        return island_count     