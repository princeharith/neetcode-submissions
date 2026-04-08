class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
            
            return True
        
        num_components = 0
        
        for node in range(n):
            if node not in visited:
                dfs(node,-1)
                num_components += 1
        
        return num_components

