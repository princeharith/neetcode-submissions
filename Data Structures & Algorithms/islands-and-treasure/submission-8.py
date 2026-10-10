class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))
        
        def addCell(r,c):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or
                grid[r][c] == -1):
                return 
            visited.add((r,c))
            q.append((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            dist += 1
        
        
        