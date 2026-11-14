class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make an adjaceny list w cost

        #minHeap, add the kth node with cost 0, do BFS w a min heap
        #push neighbor onto heap w cost 
        
        #how do we know when we've reached (keep track of nodes??)

        #Time:
        #Space:

        adj_list = defaultdict(list)
        #keep track of best time for each node
        dist = {}

        for u,v,time in times:
            adj_list[u].append((v, time))
        
        min_heap = [(0, k)] #cost, node
        dist = {}

    
        while min_heap:
            time, node =  heapq.heappop(min_heap)

            if node in dist:
                continue
            
            dist[node] = time

            for nei,cost in adj_list[node]:
                heapq.heappush(min_heap, (time+cost, nei))
        
        return max(dist.values()) if len(dist) == n else -1



        