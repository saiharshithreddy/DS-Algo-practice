'''
Idea: Create a list of deques with every deque for every diagonal
When the diagonal is at odd position the values are in the reverse order(starting from bottom) so do appendleft
when the diagonal is at even position the values are in normal order so append.

'''
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        res = [collections.deque() for i in range(row+col-1)]

        # O(MN)
        for i in range(row):
            for j in range(col):
                if (i+j)%2 == 0:
                    res[i+j].appendleft(matrix[i][j])
                else:
                    res[i+j].append(matrix[i][j])
        # O(M+N)
        flat_list = [item for sublist in res for item in sublist]
        return flat_list

        
