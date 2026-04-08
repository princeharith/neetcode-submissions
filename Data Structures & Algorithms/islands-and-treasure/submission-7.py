class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Flood fill BFS
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        print(q)
        
        while q:
            r,c,dist = q.popleft()
            for dr, dc in DIRECTIONS:
                nr,nc = dr+r, dc+c
                if (0 <= nr < rows and
                    0 <= nc < cols and 
                    grid[nr][nc] != 0 and 
                    grid[nr][nc] != -1 and
                    grid[nr][nc] > (dist + 1)):
                
                    # #then we update the grid and add 1 to dist
                    grid[nr][nc] = dist+1
                    q.append((nr, nc, grid[nr][nc]))


        