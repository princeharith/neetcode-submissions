class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # n = 5, edges = [[0,1],[1,2],[3,4]]

        # 0 <-> 1 <-> 2

        # 3 <-> 4
        
        # #go through n
        # O(V+E)
        # O(V+E)

        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        num_components = 0

        # adj_list = {
        #     0: [1]
        #     1: [0, 2]
        #     2: [1]
        #     3: [4]
        #     4: [3]
        # }

        #visited = set(0, 1, 2)

        def dfs(node):
            visited.add(node)
            
            for nei in adj_list[node]:
                if nei not in visited:
                    dfs(nei)
            
            return 
        
        for node in range(n):
            if node not in visited:
                dfs(node)
                num_components += 1
        
        return num_components
            


        
