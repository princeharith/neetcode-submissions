class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #go through each cell in grid
        #if we find a "1"
            #increment num_islands
            #mark that as a zero
            #we run a dfs from that cell
        
        #dfs helper
        #check up, down, left right, all within bounds
        #if we find a "1", we mark as zero and continue searching


        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r: int, c: int) -> None:
            for (dr, dc) in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    dfs(nr, nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = "0"
                    dfs(r,c)
        
        return num_islands
        