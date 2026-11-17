class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #start with points[0]
        #get the manhattan distance, pick the cheapest point, keep track in a set
        #bfs with a min_heap (cost is the manhattan distance)

        def get_man_distance(p1, p2):
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]

            return abs(x1-x2) + abs(y1-y2)

        n = len(points)
        adj_list = defaultdict(list)
        for i in range(n):
            for j in range(i, n):
                man_distance = get_man_distance(points[i], points[j])
                adj_list[i].append((man_distance, j))
                adj_list[j].append((man_distance, i))

        min_heap = []
        min_heap.append((0, 0)) #cost (man_distance), point
        visited_points = set()

        total_cost = 0
        while min_heap:
            cost, point = heapq.heappop(min_heap)
            if point in visited_points:
                continue
            total_cost += cost
            visited_points.add(point)
            for man_distance, nei in adj_list[point]:
                heapq.heappush(min_heap, (man_distance, nei))
        
        return total_cost

            
        