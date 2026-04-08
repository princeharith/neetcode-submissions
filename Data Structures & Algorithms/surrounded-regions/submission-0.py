class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        q = collections.deque()
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == (ROWS-1) or c == 0 or c == (COLS-1)) \
                and grid[r][c] == 'O':
                    q.append((r,c))
                    visited.add((r,c))
                    grid[r][c] = 'T'
        
        print(grid)
        def checkCell(r,c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r,c) not in visited \
            and grid[r][c] == 'O':
                q.append((r,c))
                visited.add((r,c))
                grid[r][c] = 'T'

        
        while q:
            r,c = q.popleft()
            checkCell(r+1, c)
            checkCell(r-1, c)
            checkCell(r, c+1)
            checkCell(r, c-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                elif grid[r][c] == 'T': 
                    grid[r][c] = 'O'
        
        print(grid)


