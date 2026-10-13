class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        num_rotten = 0
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        if num_fresh == 0:
            return 0
        
        #an add cell function
        def addCell(r,c):
            if ((r,c) in visited or min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1):
                    return
            nonlocal num_fresh
            num_fresh -= 1
            grid[r][c] = 2
            q.append((r,c))
            visited.add((r,c))
        
        time = -1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c-1)
                addCell(r, c+1)
            time += 1
        
        if num_fresh > 0:
            return -1
        return time

                

