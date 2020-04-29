'''
Approach: We have to traverse right, down, left, and up
1. Create a matrix
2. Traverse through the matrix and keep updating the value
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        direction = 0
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        count = 0
        while top <= bottom or right >= left:
                # move right
                if direction == 0:
                    for i in range(left, right+1):
                        matrix[top][i] = count + 1
                        count += 1
                    top += 1 # as the top row is done

                # move down

                elif direction == 1:
                    for i in range(top, bottom + 1):
                        matrix[i][right] = count + 1
                        count += 1
                    right -= 1 # as the right column is done
                elif direction == 2:
                    for i in range(right, left-1, -1):
                        matrix[bottom][i] = count + 1
                        count += 1
                    bottom -= 1
                elif direction == 3:
                    for i in range(bottom, top-1, -1):
                        matrix[i][left] = count + 1
                        count += 1
                    left += 1
                direction = (direction + 1) % 4
        return matrix
