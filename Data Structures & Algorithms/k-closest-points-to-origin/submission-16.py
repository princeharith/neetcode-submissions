class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def get_euclidean(point: int) -> float:
            x1, y1 = point
            return ((x1**2) + (y1**2))**.5
        
        euclidean_distances = []
        for i, point in enumerate(points):
            dist = get_euclidean(point)
            euclidean_distances.append((dist, i))
        
        heapq.heapify(euclidean_distances)
        
        res = []
        for _ in range(k):
            point, index = heapq.heappop(euclidean_distances)
            res.append(points[index])
        
        return res

        

        
