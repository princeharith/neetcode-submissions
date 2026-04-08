class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            if x == y:
                continue
            elif x > y:
                new_stone = x - y
                heapq.heappush(max_heap, -new_stone)
        
        return -max_heap[0] if max_heap else 0



        