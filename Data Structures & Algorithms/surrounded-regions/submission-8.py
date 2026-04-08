class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        #Os on the border
        border_set = set()
        print(board[0][COLS-1])

        for r in range(ROWS):
            if board[r][0] == "O":
                border_set.add((r,0))
            if board[r][COLS-1] == "O":
                border_set.add((r,COLS-1))

        for c in range(COLS):
            if board[0][c] == "O":
                border_set.add((0,c))
            if board[ROWS-1][c] == "O":
                border_set.add((ROWS-1,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in border_set:
                    board[r][c] = '*'

        visited = set(border_set)
        q = deque(border_set)
    

        while q:
            r,c = q.popleft()
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X':
                continue
            
            visited.add((r,c))
            board[r][c] = "O"

            if (r+1,c) not in border_set and (r+1,c) not in visited:
                q.append((r+1, c))
            if (r-1,c) not in border_set and (r-1,c) not in visited:
                q.append((r-1, c))
            if (r,c+1) not in border_set and (r,c+1) not in visited:
                q.append((r, c+1))
            if (r,c-1) not in border_set and (r,c-1) not in visited:
                q.append((r, c-1))
         
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "*" and (r,c) not in border_set:
                    board[r][c] = 'X'
        

        

        
        
            


        