class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        hashmap = dict()

        for num in range(n):
            hashmap[num] = []
        
        for edge in edges:
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        print(hashmap)
        
       
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for child in hashmap[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            # visited.remove(node)
            return True
            
        return dfs(edges[0][0], -1) and len(visited) == n
        
        