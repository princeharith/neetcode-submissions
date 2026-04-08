class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac_set, atl_set = set(), set()


        def dfs(visited, r, c, prev):
            #check if neighbor cell is larger
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or heights[r][c] < prev:
                return
            visited.add((r,c))
            dfs(visited, r+1, c, heights[r][c])
            dfs(visited, r-1, c, heights[r][c])
            dfs(visited, r, c+1, heights[r][c])
            dfs(visited, r, c-1, heights[r][c])
        

        for r in range(ROWS):
            dfs(pac_set, r, 0, -1)
            dfs(atl_set, r, COLS-1, -1)
        
        for c in range(COLS):
            dfs(pac_set, 0, c, -1)
            dfs(atl_set, ROWS-1, c, -1)
        
        return list(pac_set & atl_set)

        


