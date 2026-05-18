class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [num for num in nums]
        heapq.heapify(self.minHeap)
        self.k = k
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            print(self.minHeap[0])
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]




        
