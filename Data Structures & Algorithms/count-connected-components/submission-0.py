class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range (n)]
        
        visit = [False] * n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for child in adj[node]:
                if not visit[child]:
                    visit[child] = True
                    dfs(child)


        res = 0
        for node in range(n):
            if not visit[node]:
                dfs(node)
                visit[node] = True
                res += 1
        return res

        
        