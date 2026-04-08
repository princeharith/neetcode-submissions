class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        print(heap)

        for i in range(k):
            num = heapq.heappop(heap)
        
        return -num