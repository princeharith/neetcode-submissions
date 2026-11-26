class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #add each treasure chest to a queue, with distance
        #pop from queue, add 1, traverse in 4 directions and update land cell if curr_distance < grid

        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))


        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while q:
            r,c,cost = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = cost+1
                    q.append((nr,nc,cost+1))
        print(q)





        