
''' APPROACH 1 :
 copy the board, make changes in the copy, copy the result to original

# APPRAOCH 2 :
 when the value needs to be updated, we donot just change  0 to 1 / 1 to 0 but we do in increments and decrements of 2. (table explains)

#   previous value state change  current state   current value
#   0              no change     dead            0
#   1              no change     live            1
#   0              changed (+2)  live            2
#   1              changed (-2)  dead            -1'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                live_count = 0
                zero_count = 0
                directions = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
                for x, y in directions:
                    if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
                        if board[i+x][j+y] == 1:
                            live_count += 1
                if board[i][j] == 0 and live_count == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = -1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
