class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

        

    def add(self, val: int) -> int:
        self.nums.append(val)
        
        max_heap = [-num for num in self.nums]
        heapq.heapify(max_heap)
        

        
        res = 0
        for _ in range(self.k):
            res = heapq.heappop(max_heap)
        
        return -res
        
