class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #get the euclid distance
        #put (euc_distance, (x,y)) onto heap
        #loop through until heap is of size k
        #return the heap

        def get_euc_dist(point):
            x1,y1 = point
            return ((x1**2) + (y1**2))**.5
        
        min_heap = []

        for point in points:
            heapq.heappush(min_heap, (get_euc_dist(point), point))
        
        res = []
        for _ in range(k):
            euc, point = heapq.heappop(min_heap)
            res.append(point)

        
        return res
        

