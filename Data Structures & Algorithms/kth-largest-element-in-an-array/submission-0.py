class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        num = 0
        for _ in range(k):
            num = -heapq.heappop(nums)
        
        return num
        