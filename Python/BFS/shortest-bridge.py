class Solution:
    def shortestBridge(self, A: List[List[int]]):
        
        '''
        DFS + BFS
        In DFS, store the positions of the first island
        So we have a list of starting states and are end state would be any (i,j) with a 1 (second island)
        
        Using BFS we can find the shortest path between a start state and an end state
        '''
        
        def dfs(A, i,j):
            
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
                return
            
            A[i][j] = 2
            self.pos.append((i,j))
            for x,y in directions:
                dfs(A, i+x, j+y)
            return self.pos 
        
        self.pos = collections.deque()
        
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        flag = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    start_states = dfs(A,i,j)
                    flag = True
                    break
            if flag:
                break
                
        r = len(A)
        c = len(A[0])
        
        shortest_bridge = 0
        '''
        BFS for shortest path 
        
        '''
        while start_states:
            num_states = len(start_states)
            
            # for each start state check 4 directions for a 1
            for _ in range(num_states):
                i,j = start_states.popleft()
                
                for x,y in directions:
                    if i+x < 0 or i+x >= r or j+y < 0 or j+y >= c or A[i+x][j+y] == 2:
                        continue
                    # reached an island
                    if A[i+x][j+y] == 1:
                        return shortest_bridge
                    
                    # adding all newly visited cells with 0s
                    start_states.append((i+x,j+y))
                    # changing its value to not visit again
                    A[i+x][j+y] = 2
            # increment as we have moved 1 cell in all directions
            shortest_bridge += 1
            
            
            
        return -1
        
        
        
            
        
        
        
        