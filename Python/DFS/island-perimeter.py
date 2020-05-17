'''
Approach: DFS
Maintain a global perimeter and local perimeter
Observation: Islands can be disconnected.
TC: O(M*N)
SC: O(M*N) 
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
         # base case:
        if not grid:
            return 0
        
        def dfs(grid,i,j):
            
            
            perimeter = 4 # default perimeter of a square with side 1
            # check all 4 directions for any 1s and reduce perimeter
            for x,y in directions:
                if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and grid[i+x][j+y] == 1:
                    perimeter -= 1
                    
            return perimeter
        
        perimeter = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += dfs(grid,i,j)
            
        return perimeter