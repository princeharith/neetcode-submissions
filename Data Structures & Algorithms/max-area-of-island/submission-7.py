class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Input: grid = [
        # [0,0,0,0,0],
        # [1,0,1,0,1],
        # [0,1,1,0,1],
        # [0,1,0,0,1]
        # ]
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        DIRECTIONS = [(-1,0), (1, 0), (0,-1), (0,1)]

        def dfs(row: int, col: int) -> int:
            grid[row][col] = 0
            area = 1
            for dr, dc in DIRECTIONS:
                nr = row + dr
                nc = col + dc
                while (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                    area += dfs(nr, nc)
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr_area = dfs(r,c)
                    max_area = max(max_area, curr_area)
        
        return max_area

        