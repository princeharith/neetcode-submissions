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
            
            for child in adj_list[node]:
                if child == parent:
                    continue
                dfs(child, node)
        
        num_components = 0

        for i in range(n):
            if i not in visited:
                num_components += 1
                dfs(i, i)
        
        return num_components
                