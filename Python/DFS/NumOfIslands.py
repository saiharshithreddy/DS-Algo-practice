# @Author: Sai Harshith
# @Date:   31-Dec-2019-06-12
# @Last modified by:   Sai Harshith
# @Last modified time: 08-Jun-2020-20-06



'''
Time Compelxity: 0(m*n)
Space Complexity: 0(m*n)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(image, i,j):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return

            # update the value so you dont go into recursive loop
            grid[i][j] = '#'
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
        count = 0
        for i in range(len(grid)):
            # traversing through a row
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i , j)
                    count += 1
        return count
