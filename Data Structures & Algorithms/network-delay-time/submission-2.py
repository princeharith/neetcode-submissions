class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf') for _ in range(n)]
        distances[k-1] = 0

        adj_list = defaultdict(list)
        for u,v,t in times:
            adj_list[u].append((v,t))

        min_heap = []
        curr_time = 0

        for nei, time in adj_list[k]:
            heapq.heappush(min_heap, (curr_time+time, nei))

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)
            if curr_time < distances[node-1]:
                distances[node-1] = curr_time
                for nei, time in adj_list[node]:
                    heapq.heappush(min_heap, (curr_time+time, nei))
        
        return max(distances) if max(distances) != float('inf') else -1
