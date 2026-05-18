class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [num for num in nums]
        heapq.heapify(self.minHeap)
        self.k = k
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        #[2,3,3,3]]
        #k=3
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]




        
