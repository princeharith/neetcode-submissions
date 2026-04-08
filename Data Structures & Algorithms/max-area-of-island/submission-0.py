class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        self.maxArea = 0

        def dfs(row, col, area):
            self.maxArea = max(area, self.maxArea)
            if (row, col) in visited:
                return
            visited.add((row, col))

            for nr,nc in DIRECTIONS:
                new_row, new_col = row+nr, col+nc
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited \
                    and grid[new_row][new_col] == 1:
                    area += 1
                    dfs(new_row, new_col, area)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col, 1)
        
        return self.maxArea



        
        