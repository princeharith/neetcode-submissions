class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def getManDistance(p1, p2):
            x1,y1 = p1
            x2, y2 = p2
            return abs(x1-x2) + abs(y1-y2)

        adj_list = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                adj_list[i].append(j)
                adj_list[j].append(i)
        
        min_heap = [(0,0)]
        visited = set()
        res = 0

        while len(visited) < len(points):
            curr_distance, point = heapq.heappop(min_heap)
            if point not in visited:
                visited.add(point)
                res += curr_distance
                for nei in adj_list[point]:
                    heapq.heappush(min_heap, (getManDistance(points[point], points[nei]), nei))
        
        return res
