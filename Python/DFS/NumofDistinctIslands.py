# @Author: Sai Harshith
# @Date:   10-Mar-2020-15-03
# @Last modified by:   Sai Harshith
# @Last modified time: 10-Jun-2020-15-06



'''
Idea: To map any island to the coordinates [(0,0),(0,1), (1,0),(1,1)]
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # base case:
        if not grid:
            return 0

        distinct = set()

        for i in range(len(grid)):
            # traversing through a row
            for j in range(len(grid[0])):
                self.path =[]
                if grid[i][j] == 1:
                    self.dfs(grid, i , j, -i, -j)
                    # print(path)
                    distinct.add(tuple(self.path))


        return len(distinct)

    def dfs(self,grid, i , j, x, y):
            # boundary condiitons

            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:

                # Visited node values are changed
                self.path.append((i+x, j+y))
                grid[i][j] = 0
                # print(self.path)
                # Move into 4 directions
                self.dfs(grid, i+1, j, x, y)
                self.dfs(grid, i-1, j, x, y)
                self.dfs(grid, i, j+1, x, y)
                self.dfs(grid, i, j-1, x, y)
