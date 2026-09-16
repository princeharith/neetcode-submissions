class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == '.':
                    continue
                if num in row_set[r] or num in col_set[c] or num in box_set[(r//3,c//3)]:
                    return False
                row_set[r].add(num)
                col_set[c].add(num)
                box_set[(r//3,c//3)].add(num)

        return True
        