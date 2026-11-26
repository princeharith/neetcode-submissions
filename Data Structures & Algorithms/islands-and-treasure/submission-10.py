class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0)) #grid position, cost
        
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        while q:
            r,c,cost = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = cost + 1
                    q.append((nr, nc, cost+1))
        
        


        