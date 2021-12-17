class Solution:
    def shortestBridge(self, A: List[List[int]]):
        
        '''
        DFS + BFS
        In DFS, store the positions of the first island
        So we have a list of starting states and are end state would be any (i,j) with a 1 (second island)
        
        Using BFS we can find the shortest path between a start state and an end state
        
        An island is represented by a matrix with cells in the form of (i,j) 
        '''
        
        def dfs(A, i,j):
            
            if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
                return

            # updating the cell value to some random value so we do not traverse the same cell again 
            # (a way of keeping track of the visited cells)
            A[i][j] = 2 # 

            self.pos.append((i,j))
            # move in all 4 directions (left, right, up, and down) from a cell.
            for x,y in directions:
                dfs(A, i+x, j+y)
            return self.pos 
        
        # A dequeue to keep track of the list of (i,j) with value 1 in the matrix.
        self.pos = collections.deque()
        
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        flag = False
        
        # Time complexity O(n^2) to loop through a matrix AxB
        # start traversal from (0,0)
        for i in range(len(A)):
            for j in range(len(A[0])):
                # If the cell has a value 1 then it is a piece of land. Do a depth first search to find all the 
                # adjacent cells with value 1. 
                if A[i][j] == 1:
                    # start states is a list of land (i,j) 
                    start_states = dfs(A,i,j)
                    flag = True
                    break
            if flag:
                break
                
        row = len(A)
        col = len(A[0])
        
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
                    
                    # condition to check for out of boundary and not to traverse to island 1 which are marked with values 2
                    if i+x < 0 or i+x >= row or j+y < 0 or j+y >= col or A[i+x][j+y] == 2:
                        continue
                    # reached an piece of land
                    if A[i+x][j+y] == 1:
                        return shortest_bridge
                    
                    # adding all newly visited cells containing value 0 (water)
                    start_states.append((i+x,j+y))
                    # changing its value to not visit again
                    A[i+x][j+y] = 2
            # increment as we have moved 1 cell in all directions
            shortest_bridge += 1
            
        return -1
        
