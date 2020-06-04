class Solution:
    def maxDistance(self, grid: List[List[int]]):
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        r = len(grid)
        c = len(grid[0])
        
        land = collections.deque([(i,j) for i in range(r) for j in range(c) if grid[i][j] == 1])
        if len(land) == r * c or len(land) == 0: return -1 # No water or no land
        dist = 0
        
        while land:
            
            i,j = land.popleft()
            
            for x,y in directions:
                if (0 <= i + x < r and 0 <= j + y < c and grid[i+x][j+y] == 0):
                    
                    grid[i+x][j+y] = 1
                    land.append((i+x,j+y))
        
            dist += 1
        return dist-1
        
        
        
        
        