class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return
        row = len(matrix)-1
        col = len(matrix[0])-1
        direction = 0
        L,T,B,R = 0, 0, row, col
        res = []


        while T <= B and L <= R:
            # move left
            if direction == 0:
                for i in range(L,R+1):
                    res.append(matrix[T][i])
                # as the top row is traversed
                T += 1
            # move down
            elif direction == 1:
                for j in range(T,B+1):
                    res.append(matrix[j][R])
                # as the right row is traversed
                R -= 1
            # move left
            elif direction == 2:
                for i in range(R, L-1,-1):
                    res.append(matrix[B][i])
                B -= 1
            # move up
            elif direction == 3:
                for i in range(B,T-1,-1):
                    res.append(matrix[i][L])
                L += 1
            direction = (direction + 1) % 4
        return res
