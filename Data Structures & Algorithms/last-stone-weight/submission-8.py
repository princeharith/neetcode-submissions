class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones = [2,3,6,2,4]
        # stones = [6,4,3,2,2]

      

        #heapq.heapify(stones) #O(n)
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        # stones = [-6,-4,-3,-2,-2]

        while len(max_heap) >= 2:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            new_stone = stone1-stone2
            if new_stone > 0:
                heapq.heappush(max_heap, -new_stone)
        
        return -max_heap[0] if max_heap else 0
        