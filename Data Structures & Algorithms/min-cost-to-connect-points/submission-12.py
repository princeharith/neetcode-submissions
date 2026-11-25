class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #min cost, MST
        def get_man_distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        adj_list = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                adj_list[i].append((j, get_man_distance(points[i], points[j])))
                adj_list[j].append((i, get_man_distance(points[i], points[j])))
        
        
        min_heap = [(0, 0)] #cost, point
        total_cost = 0
        processed = set()
        #min_heap = [(1,4), (2,6), (3,6), (4,6)]
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in processed:
                continue
            processed.add(node)
            total_cost += cost

            for nei, cost in adj_list[node]:
                heapq.heappush(min_heap, (cost, nei))
        
        return total_cost
            


        

        