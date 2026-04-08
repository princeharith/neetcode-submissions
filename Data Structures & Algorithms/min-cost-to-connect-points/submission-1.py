class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Create adjacency list, of node: [cost_to_get_to_nei, nei]
        adj = defaultdict(list)
        for i in range(0, len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                man_dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([man_dist, j])
                adj[j].append([man_dist, i])
        print(adj)


        #Prims algo -> visited set, use minheap, add neighbor
        visited = set()
        minHeap = [[0,0]]
        res = 0

        while len(visited) < len(points):
            cost, node = heapq.heappop(minHeap)
            if node not in visited:
                visited.add(node)
                res += cost
                for c, nei in adj[node]:
                    if nei not in visited:
                        heapq.heappush(minHeap, [c, nei])

        return res

