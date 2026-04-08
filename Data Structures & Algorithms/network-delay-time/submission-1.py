class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build adj list
        adj_list = defaultdict(list)
        for src, target, cost in times:
            adj_list[src].append((target, cost))
        
        q = collections.deque()
        #node, time to reach, cost
        q.append((k, 0 ))
        
        min_time = [float('inf')] * n
        min_time[k-1] = 0

        while q:
            curr_node, curr_time = q.popleft()
            for target, cost in adj_list[curr_node]:
                if curr_time + cost < min_time[target-1]:
                    min_time[target-1] = curr_time + cost
                    q.append((target, curr_time + cost))
        if float('inf') in min_time:
            return -1
        return max(min_time)

