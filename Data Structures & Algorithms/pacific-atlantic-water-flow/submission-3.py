class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Input: heights = [
        # [4,2,7,3,4],
        # [7,4,6,4,7],
        # [6,3,5,3,6]
        # ]

        #find everything that can flow into the pacific
        #find everything that can flow into the atlantic, combine them

        ROWS = len(heights)
        COLS = len(heights[0])

        DIRECTIONS = [(1,0), (-1,0), (0,-1), (0,1)]
        

        def dfs(r,c,ocean_set):
            if (r,c) in ocean_set:
                return 
            ocean_set.add((r, c))

            for dr, dc in DIRECTIONS:
                if (0 <= r+dr < ROWS and 
                    0 <= c+dc < COLS and 
                    (r+dr, c+dc) not in ocean_set and
                    (heights[r+dr][c+dc] >= heights[r][c])):
                    
                    dfs(r+dr, c+dc, ocean_set)
        
        pac_set = set()
        atl_set = set()
        for r in range(ROWS):
            dfs(r, 0, pac_set)
            dfs(r, COLS-1, atl_set)
        
        for c in range(COLS):
            dfs(0, c, pac_set)
            dfs(ROWS-1, c, atl_set)
        
        print(pac_set)
        print(atl_set)
        
        return list(pac_set & atl_set)

        
        


                    


        
        
        

