class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        visited = set()
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node,parent):
            if node in visited:
                return False

            visited.add(node)

            for child in adj_list[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n
        