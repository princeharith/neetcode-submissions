class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        memo = {}

        def backtrack(r,c):
            if r >= ROWS or c >= COLS:
                return float('inf')
            
            if r == (ROWS - 1) and c == (COLS - 1):
                return grid[r][c]
            
            if (r,c) in memo:
                return memo[(r,c)]
            
            
            #at each point, we take the current val and go up, 
            #or we take the current val and go down
            memo[(r,c)] = grid[r][c] + min(backtrack(r+1, c), backtrack(r, c+1))
            return memo[(r,c)]
            
        return backtrack(0,0)

        