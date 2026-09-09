class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for the tricky box index, the key can be a tuple (r//3, c//3)
        #e.g. box (0,0), box (0,1), box (0,2) etc etc
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in row_set[r]:
                    return False
                elif board[r][c] in col_set[c]:
                    return False
                elif board[r][c] in box_set[(r//3, c//3)]:
                    return False
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_set[(r//3, c//3)].add(board[r][c])
        
        return True

                
        