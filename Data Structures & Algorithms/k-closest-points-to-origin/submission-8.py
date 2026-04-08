class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x,y):
            dist = math.sqrt((x**2)+(y**2))
            return dist
        
        distances = []
        for point in points:
            distances.append((getDistance(point[0], point[1]), [point[0], point[1]]))
        
        heapq.heapify(distances)
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(distances)[1])
        return res
        

        

