'''
Approach: 
Similar to #490. The Maze
Keep note of the distance

Case: From point A to B the distance is 6 and from point C to B the distance is 5 and some part of the path (C->B) matches 
with the path (A->B) then instead of just checking if the cell is visited or not we have to check if the distance from the new path
is less than the prev path. 

TC: O(MN * max(M,N))
'''
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]):
        queue = collections.deque()
        
        queue.append((start[0], start[1],0))    
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        path = 0
        res =[]
        visited = collections.defaultdict(int)
        visited[(start[0], start[1])] = 0 
        shortest_dist = float('inf')
        while queue:

            i, j, dist = queue.popleft()
            if i == destination[0] and j == destination[1]:
                shortest_dist = min(shortest_dist, dist)

            # roll the ball in one direction until it reaches a wall (1)
            for x,y in directions:
                r, c = i+x, j+y
                dist_new = dist
                while 0<= r< len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != 1:
                    dist_new += 1
                    r += x
                    c += y
                # roll back 
                r -= x
                c -= y

                # add it to visited and if a path to this cell has a distance greater than the current path distance.
                if (r,c) not in visited or (r,c) in visited and visited[(r,c)] > dist_new:    
                    # add the cell to the queue
                    queue.append((r,c, dist_new))
                    # update the distance 
                    visited[(r,c)] = dist_new
             
        return shortest_dist if shortest_dist != float('inf') else -1