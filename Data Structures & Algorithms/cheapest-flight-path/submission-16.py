class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #keep track of stops
        # src -> A -> dst

        # k = 1
        min_stops = [float('inf')] * n

        #keep track of the airport, how many stops we are at, and the cost

        adj_list = defaultdict(list)
        for from_airport, to_airport, cost in flights:
            adj_list[from_airport].append((to_airport, cost))
        
        min_heap = [(0, src, 0)] #cost, airport, stops
       
        
        while min_heap:
            cost, curr_airport, stops = heapq.heappop(min_heap) 
            if curr_airport == dst:
                return cost

            
            if stops >= min_stops[curr_airport]:
                continue

            min_stops[curr_airport] = stops
           
            for nei, cost_to_go in adj_list[curr_airport]:
                if stops <= k:
                    heapq.heappush(min_heap, (cost+cost_to_go, nei, stops+1))
        
        
        return -1

        


        