class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        
        print(q)
        
        while q:
            r,c,dist = q.popleft()
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or dist > grid[r][c]):
                continue

    

            grid[r][c] = dist

            q.append((r+1,c,dist+1))
            q.append((r-1,c,dist+1))
            q.append((r,c-1,dist+1))
            q.append((r,c+1,dist+1))
        
        
            



        