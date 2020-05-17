class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0    
        max_area = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = 1 if matrix[i][j] == '1' else 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    if i != 0 and j != 0:
                        val = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                        matrix[i][j] = val
                    else:
                        val = matrix[i][j]
                    max_area = max(max_area, val)
        
        return max_area * max_area