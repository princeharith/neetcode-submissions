class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        fresh = 0



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row,col))
                    visited.add((row,col))
                if grid[row][col] == 1:
                    fresh += 1
        

        def checkCell(row,col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and \
            (row,col) not in visited and grid[row][col] == 1:
                    grid[row][col] = 2
                    q.append((row,col))
                    visited.add((row,col))
                    nonlocal fresh
                    fresh -= 1
  
        num_seconds = 0
        while q and fresh > 0 :
            for _ in range(len(q)):
                row,col = q.popleft()
                checkCell(row+1, col)
                checkCell(row-1, col)
                checkCell(row, col-1)
                checkCell(row, col+1)
            num_seconds += 1

            
        
        return num_seconds if fresh == 0 else -1




