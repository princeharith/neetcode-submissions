class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #set for row, set for col, set for box
        row_set = [set() for _ in range(len(board))]
        col_set = [set() for _ in range(len(board[0]))]
        box_set = [set() for _ in range(len(board))]
    
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
            
                if board[r][c] in row_set[r]:
                    return False
                if board[r][c] in col_set[c]:
                    return False
                
                box_idx = ((r//3) * 3) + (c//3)
                if board[r][c] in box_set[box_idx]:
                    return False
                
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_set[box_idx].add(board[r][c])
        
        return True
