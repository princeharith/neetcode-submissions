class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #go through rows and cols
        #if we encounter an 'O', add to visited, and run dfs

        #dfs
            #if all neighbors are good, then flip back to Xs
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r in (0, ROWS-1) or c in (0, COLS-1)):
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        