class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #man_distance/cost = abs(x1-x2) + abs(y1-y2)
        def getManDistance(p1, p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2) + abs(y1-y2)

        #create edges
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                edges.append((i,j))
        
        adj_list = defaultdict(list)
        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        #adj_list = {
            # 0: 1,2,3,4
            # 1: 2,3,4
            # 2: 3,4
            # 3: 4

        #}
        #add the first point
        min_heap = []
        min_heap.append((0,0))

        visited = set()
        #visited = set(0,()))
        res = 0

        while min_heap:
            curr_dist, point = heapq.heappop(min_heap)
            if point not in visited:
                visited.add(point)
                res += curr_dist
                
                for nei in adj_list[point]:
                    if nei not in visited:
                        manDist = getManDistance(points[point], points[nei])
                        heapq.heappush(min_heap, (manDist, nei))
            
        return res

        
        
        
