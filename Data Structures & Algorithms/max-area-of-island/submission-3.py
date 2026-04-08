class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c,curr_area):
            print(r,c)
            if (0 > r or r >= ROWS or
                0 > c or c >= COLS or
                grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            curr_area = 1

            curr_area += dfs(r+1,c,curr_area+1)
            curr_area += dfs(r-1,c,curr_area+1)
            curr_area += dfs(r,c+1,curr_area+1)
            curr_area += dfs(r,c-1,curr_area+1)

            return curr_area
            
        
                
            
        max_island_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_island_area = max(dfs(r,c,0), max_island_area)
        return max_island_area
        