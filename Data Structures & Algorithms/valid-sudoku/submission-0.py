class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        row_set, col_set, box_set = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]

        for r in range(rows):
            for c in range(cols):
                box_idx = (c//3) + ((r//3) * 3)
                if board[r][c] == '.':
                    continue
                elif board[r][c] in row_set[r]:
                    print("found in row_set")
                    print(board[r][c])
                    print(row_set)
                    print(row_set[r])
                    return False
                elif board[r][c] in col_set[c]:
                    return False
                elif board[r][c] in box_set[box_idx]:
                    return False
                element = board[r][c]
                row_set[r].add(element), col_set[c].add(element), box_set[box_idx].add(element)
        
        return True


        