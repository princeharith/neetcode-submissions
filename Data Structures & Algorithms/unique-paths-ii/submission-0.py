class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        memo = {}
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        def backtrack(r,c):
            if r >= ROWS or c >= COLS:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if r == ROWS-1 and c == COLS-1:
                return 1
            
            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = backtrack(r+1, c) + backtrack(r, c+1)
            return memo[(r,c)]

        return backtrack(0,0)  



        # [0,0,0]
        # [0,0,0] 
        # [0,1,0]         