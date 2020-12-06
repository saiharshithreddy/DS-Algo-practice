'''
Approach: BFS 

Observation: The ball rolls over till it hits a wall. 
'''
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]):
        queue = collections.deque()
        
        queue.append((start[0], start[1]))
        found = False
        maze[start[0]][start[1]] = 2
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            
            i, j = queue.popleft()
            print('pop', (i,j))

            if i == destination[0] and j == destination[1]:
                return True

            for x,y in directions:
                r, c = i+x, j+y

                while 0<= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1:
                    r += x
                    c += y
                r -= x
                c -= y
                if maze[r][c] == 0:    
                    queue.append((r,c))
                    maze[r][c] = 2
                
        return False
                