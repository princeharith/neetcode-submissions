class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Create edges arbitrarily, i.e. 0--->1 represents the dist between points[0] and points[1]
        adj = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(1, len(points)):
                x2, y2 = points[j]
                man_distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append((man_distance, j))
                adj[j].append((man_distance, i))
        
        
        #Initialize heap, res, and set
        minHeap = [(0,0)]
        res = 0
        visited = set()

        #Push and pop from our heap
        while len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)
            if point not in visited:
                visited.add(point)
                res += cost
                for c,nei in adj[point]:
                    if nei not in visited:
                        heapq.heappush(minHeap, (c, nei))
        
        return res
                

        

            

        