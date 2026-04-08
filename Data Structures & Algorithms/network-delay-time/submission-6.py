class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make an adjacency list, with node and 'weight'
        #use a min heap to always take the edge that is fastest?
        #use a visited set, once we pop from the heap, that is the smallest path

        #bottleneck is the node that has the longest min time associated it with it, as
        #that determines the time it takes for all nodes to receive the signal

        adj_list = defaultdict(list)
        for u,v,t in times:
            #each tuple within is of time, v
            adj_list[u].append((t, v))
        
        visited = set()
        #we want the time, node in the heap
        min_heap = [(0,k)]

        res = [float('inf')] * n

        while min_heap:
            print(min_heap)
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            res[node-1] = time
            visited.add(node)

            for t, nei in adj_list[node]:
                if nei in visited:
                    continue
                heapq.heappush(min_heap, (time+t, nei))
        
        print(res)
        ans = max(res)
        return ans if ans != float('inf') else -1


        """
        t, nei = 
        min_heap = [(3, 4), (4,4)]

        visited = {0,1, 2 }
        time, node = 2, 3
        res = [0,1,2,inf]
        
        

        """
            


        
        