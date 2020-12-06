class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. Swap 1st row with nth row, 2nd row with n-1th row and so on.
        start = 0
        end = len(matrix)-1

        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1

        # 2. Swap values on either sides of the diagonal
        for i in range(len(matrix)):
            # j < i
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
