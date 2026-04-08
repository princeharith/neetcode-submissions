class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        distance_to_point_map = defaultdict(list)
        
        def get_distance(x,y):
            return math.sqrt((x**2)+(y**2))
        
        for point in points:
            x,y = point[0],point[1]
            distances.append(get_distance(x,y))
            distance_to_point_map[get_distance(x,y)].append(point)
        
        
        #heapq.heapify(distances)
        distances.sort()
        print(distances)
        print(distance_to_point_map)

        res = []
        for dist in distances:
            for point in distance_to_point_map[dist]:
                res.append(point)
                if len(res) == k:
                    return res