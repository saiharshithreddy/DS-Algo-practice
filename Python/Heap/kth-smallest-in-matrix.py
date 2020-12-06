import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        minheap = []
        for i in range(len(matrix)):
            heapq.heappush(minheap, (matrix[i][0],0, matrix[i]))

        count = 0
        while minheap:
            number, i, row = heapq.heappop(minheap)
            count += 1

            if count == k:
                break

            if len(row) > i+1:
                heapq.heappush(minheap, (row[i+1], i+1, row))

        return number

        
