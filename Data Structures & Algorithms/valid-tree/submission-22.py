class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n = len(edges)+1
        if len(edges) != n-1:
            return False
        par = [i for i in range(n)]
        size = [1] * n

        def find(x):
            while x != par[x]:
                x = par[x]
            return x
        
        def union(a, b):
            par_a, par_b = find(a), find(b)
            if par_a == par_b:
                return False
            if size[par_a] < size[par_b]:
                par_a, par_b = par_b, par_a

            par[par_b] = par_a
            size[par_a] += size[par_b]
            return True
        
        for a,b in edges:
            if not union(a, b):
                return False
        return True
        