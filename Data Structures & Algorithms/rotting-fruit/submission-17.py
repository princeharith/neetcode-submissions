class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #keep track of the fruits
        #search starting from a rotten fruit (BFS w a q)
        #slowly update grid/update fresh fruit count w mins
        #if 0 fresh fruits -> return mins or -1

        ROWS, COLS = len(grid), len(grid[0])
        #q should keep track of r,c,current_minute
        q = deque()

        fresh_fruits = 0
        rotten_count = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    rotten_count += 1
                    q.append((r,c,0))

        if fresh_fruits == 0 and rotten_count == 0:
            return 0
        
        while q:
            r,c,minutes = q.popleft()
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0 or grid[r][c] == '*'):
                continue
            if grid[r][c] == 1:
                fresh_fruits -= 1
            grid[r][c] = '*'
            q.append((r+1,c,minutes+1))
            q.append((r-1,c,minutes+1))
            q.append((r,c+1,minutes+1))
            q.append((r,c-1,minutes+1))
        print(fresh_fruits)
        
        return minutes-1 if fresh_fruits == 0 else -1
            



        