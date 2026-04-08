class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {}
        for i in range(n):
            adj_list[i] = []

        for i in range(len(flights)):
            frm, to, cost = flights[i]
            adj_list[frm].append((to, cost))

        q = deque()
        q.append((src, 0, 0))

        best_cost = [float('inf')] * n
        best_cost[src] = 0

        while q:
            airport, curr_cost, curr_stops = q.popleft()
            for neighbor, cost in adj_list[airport]:
                new_cost = curr_cost + cost
                if curr_stops <= k and new_cost <= best_cost[neighbor]:
                    best_cost[neighbor] = new_cost
                    q.append((neighbor, new_cost, curr_stops+1))
        

        if best_cost[dst] == float('inf'):
            return -1
        else:
            return best_cost[dst]
                

        
