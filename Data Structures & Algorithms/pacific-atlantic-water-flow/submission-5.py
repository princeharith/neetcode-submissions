class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        #we check what cells flow to pacific
        #check what cells flow to atlantic

        #and then combine the coords

        rows, cols = len(heights), len(heights[0])
        pacific_coords = []
        atlantic_coords = []
        for c in range(cols):
            pacific_coords.append((0,c))
            atlantic_coords.append((rows-1,c))

        for r in range(rows):
            pacific_coords.append((r,0))
            atlantic_coords.append((r,cols-1))
        
        
        DIRECTIONS = [(0,1), (0,-1), (-1,0), (1,0)]



        def dfs(r,c, ocean_set):
            ocean_set.add((r,c))
            for dr, dc in DIRECTIONS:
                nr, nc = r+dr, c+dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    (nr,nc) not in ocean_set and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, ocean_set)

            
        
        pacific_set = set()
        for r,c in pacific_coords:
            dfs(r,c, pacific_set)

        atlantic_set = set()
        for r,c in atlantic_coords:
            dfs(r,c,atlantic_set)
        
        res = []

        for (r,c) in pacific_set:
            if (r,c) in atlantic_set:
                res.append((r,c))
        
        return res
        

        
        
            

        