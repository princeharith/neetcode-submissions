class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #get distances
        #push them onto the heap
        #finally the k points

        def getDistance(point):
            x,y = point[0], point[1]
            return math.sqrt(x**2 + y**2)
        
        min_heap = []
        res = []
        for point in points:
            heapq.heappush(min_heap, (getDistance(point), point))
        
        
        for _ in range(k):
            _, point = heapq.heappop(min_heap)
            res.append(point)
        
        return res
