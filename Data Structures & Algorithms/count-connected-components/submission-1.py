class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        num_components = 0
        adj_list = defaultdict(list)
        
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)
            
        for node in range(n):
            if node not in visited:
                num_components += 1
                dfs(node)
        
        return num_components

