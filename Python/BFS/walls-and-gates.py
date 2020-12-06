class Solution:
    def wallsAndGates(self, rooms: List[List[int]]):
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        Start state: Gate
        End state: Empty room
        BFs
        '''
        if not rooms: return 
        r = len(rooms)
        c = len(rooms[0])
        queue = collections.deque([(i,j) for i in range(r) for j in range(c) if rooms[i][j] == 0])
        print(queue)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue:
            
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for x, y in directions:
                    p, q = i+x, j+y
                    if 0<= p < r and 0 <= q < c and (rooms[p][q] != -1 and rooms[p][q] != 0):
                        
                        if rooms[p][q] == 2147483647:
                            rooms[p][q] = rooms[i][j]+1    
                            queue.append((p,q))
                            
                        
        
                        
            
            
        