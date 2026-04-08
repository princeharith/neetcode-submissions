import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Build adjacency list: node -> list of (neighbor, cost)
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        
        # Min-heap: (total_cost, current_city, stops)
        heap = [(0, src, 0)]
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # If we reached destination within allowed stops
            if node == dst:
                return cost
            
            # If we can still take more stops
            if stops <= k:
                for nei, price in graph[node]:
                    heapq.heappush(heap, (cost + price, nei, stops + 1))
        
        return -1
