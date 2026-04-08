class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        num_islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                for d1, d2 in directions:
                    new_row, new_col = r + d1, c + d2

                    if new_row < 0 or new_col < 0 or new_row >= rows or \
                        new_col >= cols or (new_row,new_col) in visited or grid[new_row][new_col] == '0':
                        continue
                    visited.add((new_row,new_col))
                    q.append((new_row,new_col))
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    num_islands += 1
        
        return num_islands