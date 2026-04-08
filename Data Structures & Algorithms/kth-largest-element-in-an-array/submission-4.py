class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        kth_largest = 0
        for _ in range(k):
            kth_largest = heapq.heappop(max_heap)
        
        return -kth_largest


        