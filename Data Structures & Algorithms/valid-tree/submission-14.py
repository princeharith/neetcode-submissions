class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        
        visited = set()
        def dfs(curr, src):
            if curr in visited:
                return False
            visited.add(curr)

            for nei in adj_list[curr]:
                if nei == src:
                    continue
                if not dfs(nei, curr):
                    return False

            return True

        res = dfs(0, 0)
        if len(visited) != n:
            return False
        return res
        
        


        