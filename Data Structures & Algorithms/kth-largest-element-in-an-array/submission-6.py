class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        for _ in range(k):
            item = heapq.heappop(heap)
        
        return -item