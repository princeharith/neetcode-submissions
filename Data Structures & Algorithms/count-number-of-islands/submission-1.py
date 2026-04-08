class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        #UP, DOWN, LEFT, RIGHT
        DIRECTIONS = [[-1, 0], [1,0], [0, -1], [0,1]]
        num_islands = 0

        def bfs(row, col):
            for r,c in DIRECTIONS:
                new_row = row+r
                new_col = col+c

                if new_row >= 0 and new_row < rows and \
                new_col >= 0 and new_col < cols and grid[new_row][new_col] == '1' and \
                (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    bfs(new_row, new_col)





        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    print("1 found!")
                    print((row,col))
                    visited.add((row, col))
                    num_islands += 1
                    bfs(row, col)
        
        return num_islands
            

        