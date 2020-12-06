class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        # similar to number of islands
        
        
        def dfs(board,i,j):
            # out of board
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'E'
            dfs(board,i+1,j)
            dfs(board,i-1,j)
            dfs(board,i,j+1)
            dfs(board,i,j-1)
            
        # dfs call only on borders
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0]) - 1:
                    if board[i][j] == 'O':
                        dfs(board, i,j)
                        
        # check for O and convert to X and E to O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':     
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'
    