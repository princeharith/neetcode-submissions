class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        cycleStart = -1
        cycle = set()

        recursion_depth = 0


        def dfs(node, parent):

            nonlocal cycleStart
            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
                    
            return False


        dfs(1,-1)

        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
