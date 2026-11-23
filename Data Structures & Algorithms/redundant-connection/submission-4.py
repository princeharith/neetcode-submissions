class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        par = [i for i in range(n)]
        size = [1] * n

        def find(x):
            while x != par[x]:
                x = par[x]
            return x
        
        def union(a, b):
            par_a, par_b = find(a), find(b)

            #same parent
            if par_a == par_b:
                return False
            
            if size[par_a] < size[par_b]:
                par_a, par_b = par_b, par_a
            size[par_a] += size[par_b]
            par[par_b] = par_a
            return True

        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        


