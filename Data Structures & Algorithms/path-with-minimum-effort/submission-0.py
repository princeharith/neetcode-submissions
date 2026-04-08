class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # src = 0,0
        # node = (r,c)
        # neighbors are:
        #     up down left right
        # effort = diff in heights

        DIRECTIONS = [[1,0], [0,1], [0,-1], [-1,0]]

        min_heap = []
        #push the node and the weight
        heapq.heappush(min_heap, (0, (0,0)))
        #visited set so we dont revisit
        visited = set()

        while min_heap:
            diff, coord = heapq.heappop(min_heap)

            if coord in visited:
                continue
            visited.add(coord)

            r,c = coord
            if r == len(heights)-1 and c == len(heights[0])-1:
                return diff

           

            for dr, dc in DIRECTIONS:
                nr,nc = r+dr, c+dc
                if (0 <= nr < len(heights) and 
                    0 <= nc < len(heights[0]) and
                    (nr,nc) not in visited):

                    worst_edge = max(abs(heights[r][c] - heights[nr][nc]), diff)

                    heapq.heappush(min_heap, (worst_edge, (nr,nc)))
        





