class Solution:
    def minKnightMoves(self, x: int, y: int):
        
        '''
        BFS 
        '''
        queue = collections.deque()
        x = abs(x)
        y = abs(y)
        queue.append((0,0,0))
        visited = set()
        visited.add((0,0))
        # end state = (x,y)
        dist = 0
        directions = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        while queue:
            
            i,j, dist = queue.popleft()
            if i== x and j == y:
                return dist

            for a,b in directions:
                m,n = i+a,j+b

                if (m,n) not in visited and m >-4 and n >-4:
                    
                    queue.append((m,n,dist+1))
                    visited.add((m,n))
            
        return dist
        
        