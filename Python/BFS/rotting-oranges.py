class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        queue = collections.deque()
        num_fresh = 0

        for i in range(row):
            for j in range(col):

                # check for fresh oranges
                if grid[i][j] == 1:
                    num_fresh += 1
                # add rotten oranges to queue
                elif grid[i][j] == 2:
                    queue.append((i,j))

        mins = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while queue:

            for _ in range(len(queue)):
                i,j = queue.popleft()
                # check for all four directions for fresh oranges

                for x, y in directions:
                    if 0<= i+x < row and 0<= j+y < col:

                        if grid[i+x][j+y] == 1:

                            grid[i+x][j+y] = 2
                            num_fresh -= 1
                            queue.append((i+x,j+y))

            mins += 1

        return max(0,mins-1) if num_fresh == 0 else -1
                
