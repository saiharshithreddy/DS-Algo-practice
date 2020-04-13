class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    res.append([i,j])
        # print(res)
        row = len(matrix)
        col = len(matrix[0])

        for i, j in res:
            n , m = 0, 0
            while n < row:
                matrix[n][j] = 0
                n += 1
            while m < col:
                matrix[i][m] = 0
                m += 1
