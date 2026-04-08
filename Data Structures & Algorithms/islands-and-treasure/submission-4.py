class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        q = collections.deque()
        visited = set()
        dist = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))

        
        def check_coord(r,c, dist):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and \
             grid[r][c] != -1 and (r,c) not in visited:
                q.append((r,c))
                visited.add((r,c))
                grid[r][c] = dist
        

        while q:
            q_len = len(q)
            dist += 1
            for _ in range(q_len):
                r, c = q.popleft()
                check_coord(r+1, c, dist)
                check_coord(r-1, c, dist)
                check_coord(r, c-1, dist)
                check_coord(r, c+1, dist)
