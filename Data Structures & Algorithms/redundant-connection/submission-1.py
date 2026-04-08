class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visiting = set()
        res = []

        def dfs(node, parent):
            if node in visiting:
                print(f'visiting is {visiting}')
                res.append(visiting)
                return False
            
            visiting.add(node)
            
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            visiting.remove(node)
            return True
        
        dfs(edges[0][0], -1)
        
        for i in range(len(edges)-1, -1, -1):
            u,v = edges[i]
            if u in res[0] and v in res[0]:
                return edges[i]

        
        # -> children of 1 
        #     -> 2
        #         -> 1 (it is parent so skip)
        #         -> 4
        #             -> 2 (parent so skip)
        #             -> 3 
        #                 -> 1 cycle found (component with parent 4 has cycle)
       
        

        #  -> children of 1 
        #     -> 2
        #         -> 1 (it is parent so skip)
        #     -> 3
        #         -> 1 (parent so skip)
        #         -> 4 
        #             -> 1 cycle found (component with parent 4 has cycle)
        #     -> 3   

        # #find start and end of component with cycle, return last edge


