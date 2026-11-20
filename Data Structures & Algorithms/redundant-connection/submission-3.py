class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #keep track of parents
        n = len(edges)
        par = [i for i in range(n+1)] #[0,1,1,1,1]
        # par = [0,1,1,2,2]
        size = [1] * (n+1)

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            size[ra] += size[rb]
            par[rb] = ra
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        
        

        