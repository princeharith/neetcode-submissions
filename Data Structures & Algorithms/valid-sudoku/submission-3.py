class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check all rows, need a set for each row
        #whats it called when lists/sets aren't distinct?
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sub_set = [set() for _ in range(9)]
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                print(row_set)
                sub_index = (r//3 + c//3) + (2 * (r//3))
                if board[r][c] in row_set[r]:
                    return False
                elif board[r][c] in col_set[c]:
                    return False
                elif board[r][c] in sub_set[sub_index]:
                    return False
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                sub_set[sub_index].add(board[r][c])

        return True