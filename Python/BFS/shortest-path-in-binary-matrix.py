class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]):
        # edge cases
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        
        queue = collections.deque()
        
        queue.appendleft((0,0,1))
        # 8 directions
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        r = len(grid)-1
        c = len(grid[0])-1
        
        count = 1
        '''
        BFS for shortest path
        '''
        while queue:
            i,j, path_len = queue.popleft()
            
            # reached the cell (r,c)
            if i == r and j == c:
                return path_len
            
            for x,y in directions:
                if 0 <= i+x <= r and 0 <= j+y <= c and grid[i+x][j+y] ==0 :
                    # if the cell is 0
                    queue.append((i+x,j+y,path_len+1))
                    # change its value so to make it visited
                    grid[i+x][j+y] = 2
                      
        return -1
                
            