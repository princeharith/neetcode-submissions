class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #build adjacency list
        #keep track of visited nodes (with a list), keep track of cycle, and if cycle has started
        adj_list = defaultdict(list)
        # adj_list = [[] for _ in range(len(edges)+1)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = [False] * (len(edges)+1)
        cycle = set()
        cycleStart = -1

        def dfs(node, parent):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            
            visited[node] = True
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True
            return False


        dfs(1, -1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        
        return []

        #dfs -> we return True or False depending on if node is in a cycle
            #if node has already been visited, cycle has started
        

            
        