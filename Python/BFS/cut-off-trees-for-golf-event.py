# @Author: Sai Harshith
# @Date:   24-May-2020-20-05
# @Last modified by:   Sai Harshith
# @Last modified time: 24-May-2020-20-05

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:

        def bfs(forest, src, di, dj):
            queue = collections.deque()
            queue.append((src[0],src[1], 0))
            visited = {(src[0], src[1])}


            while queue:
                i,j,steps = queue.popleft()
                if i == di and j == dj:
                    return steps
                for x, y in [[0,1],[0,-1],[1,0],[-1,0]]:
                    r, c = i+x, j+y

                    if 0<= r < len(forest) and 0<= c < len(forest[0]) and forest[r][c] != 0 and (r,c) not in visited:
                        visited.add((r,c))
                        queue.append((r,c, steps+1))

            return -1


        tree_loc = collections.deque()
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    tree_loc.append((forest[i][j], i,j))

        tree_loc = sorted(tree_loc, key=lambda x: x[0])

        total_steps = 0
        start = (0,0)
        for _, di, dj in tree_loc:
            steps = bfs(forest, start, di, dj)
            if steps < 0: return -1
            total_steps += steps
            start = (di,dj)
        return total_steps








                                
