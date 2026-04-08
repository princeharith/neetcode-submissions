class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u, v, w in times:
            adj_list[u].append((w, v))
        
        minHeap = [(0, k)]
        visited = set()
        #cost of going to that last node
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for w2, n2 in adj_list[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (t+w2, n2))
        
        return t if len(visited) == n else -1