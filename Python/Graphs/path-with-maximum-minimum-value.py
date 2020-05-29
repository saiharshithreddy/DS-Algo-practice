# @Author: Sai Harshith
# @Date:   27-May-2020-12-05
# @Last modified by:   Sai Harshith
# @Last modified time: 27-May-2020-12-05

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        '''
        Time: O(MN log MN)
        space: O(MN)
        '''
        row = len(A)
        col = len(A[0])

        maxheap = []
        heappush(maxheap, (-A[0][0], 0, 0))

        visited = set()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while maxheap:
            val, i, j = heapq.heappop(maxheap)
            if i == row - 1 and j == col - 1:
                return -val
            for x, y in directions:
                if i + x >= 0 and i + x < row and j + y >= 0 and j + y < col and (i+x, j+y) not in visited:
                    visited.add((i + x,j + y))
                    heapq.heappush(maxheap,
                                   (max(val, -A[i + x][j + y]), i + x, j + y))
        return -1
