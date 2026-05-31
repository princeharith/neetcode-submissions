class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #get distances
        #push them onto the heap
        #finally the k points

        def getDistance(point):
            x,y = point[0], point[1]
            return math.sqrt(x**2 + y**2)
        
        max_heap = []
        res = []
        for point in points:
            heapq.heappush(max_heap, (-getDistance(point), point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [point for dist, point in max_heap]
        
        
        return res
