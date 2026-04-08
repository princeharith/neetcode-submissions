class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #loop through the nodes from 0 to n-1
            #undirected, so will need an adj list
        #if node not in visited_before,
            #increment num_components
            #run dfs on that node, add nodes to big visited set
        
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return True
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)
            
            # return True
        num_components = 0
        for node in range(n):
            if node not in visited:
                num_components += 1
                dfs(node, -1)
        return num_components

        