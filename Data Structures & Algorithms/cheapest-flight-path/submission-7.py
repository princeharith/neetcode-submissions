class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u,v,w in flights:
            adj_list[u].append((v,w))
        
        src_to_dest = [float('inf')] * n
        min_heap = []
        heapq.heappush(min_heap, (0,src, k))


        #go through neighbors
        while min_heap:
            curr_cost, airport, stopsleft = heapq.heappop(min_heap)
            if stopsleft < -1:
                continue
            
            src_to_dest[airport] = min(src_to_dest[airport], curr_cost)

            for nei,weight in adj_list[airport]:
                if curr_cost + weight < src_to_dest[nei]:
                    heapq.heappush(min_heap, (curr_cost+weight, nei, stopsleft-1))
        
        return src_to_dest[dst] if src_to_dest[dst] != float('inf') else -1
