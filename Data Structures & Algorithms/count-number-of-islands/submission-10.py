class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #go through each r,c
            #if its a 1 (land), increase number of islands
            #dfs from that spot, flip all connected 1s to 0s
        #return the number of islands


        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            while q:
                row,col = q.popleft()
                directions = [[1,0], [0,1], [0,-1], [-1,0]]
                for dr, dc in directions:
                    new_row = (row+dr)
                    new_col = (col+dc)

                    #check if its in bounds
                    if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])) and (grid[new_row][new_col] == '1'):
                        grid[new_row][new_col] = '0'
                        q.append((new_row, new_col))

        num_islands = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    num_islands += 1
                    bfs(r,c)
        
        return num_islands

        