class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        DIRECTIONS = [(0,1), (0,-1), (-1,0), (1,0)]
        pac_flow = [[False] * cols for r in range(rows)]
        atl_flow = [[False] * cols for r in range(rows)]

        
        def bfs(coords, ocean):
            q = collections.deque(coords)
            while q:
                r,c = q.popleft()
                ocean[r][c] = True
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    new_r, new_c = r+dr, c+dc
                    if (new_r >= 0 and new_c >= 0 and new_r < rows and new_c < cols and 
                        ocean[new_r][new_c] == False and heights[new_r][new_c] >= heights[r][c]):
                        q.append((new_r,new_c))

        pacific_flow_coords = []
        atlantic_flow_coords = []

        for r in range(rows):
            pacific_flow_coords.append((r,0))
            atlantic_flow_coords.append((r, cols-1))
        
        for c in range(cols):
            pacific_flow_coords.append((0,c))
            atlantic_flow_coords.append((rows-1, c))

        bfs(pacific_flow_coords, pac_flow)
        bfs(atlantic_flow_coords, atl_flow)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if pac_flow[r][c] and atl_flow[r][c]:
                    res.append((r,c))
        
        return res


       

        