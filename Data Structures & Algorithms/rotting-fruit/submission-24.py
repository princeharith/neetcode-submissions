class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #add rotten fruits to a queue
        #increase time
            #as we pop, check neighbors. If fresh, decrease fresh count, add them to queue

        #if rotten == fresh, return time
        #else, return -1
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        t = 0
        while q:
            q_len = len(q)
            t += 1
            for _ in range(q_len):
                r2,c2 = q.popleft()
                for dr,dc in DIRECTIONS:
                    nr = r2+dr
                    nc = c2+dc

                    if (0 <= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh_count -= 1

                        q.append((nr,nc))
        
        return t-1 if fresh_count == 0 else -1
            



