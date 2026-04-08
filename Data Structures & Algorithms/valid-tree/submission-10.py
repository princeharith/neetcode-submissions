class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges == []:
            return True
        visited = set()
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(node,parent):
            print(f'{node}, {parent}')
            if adj_list[node] == []:
                return True
            if node in visited:
                print(f"node {node} with parent {parent} is visited")
                print(f"node {node} is visited")
                return False

            visited.add(node)

            for child in adj_list[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            
            adj_list[node] = []
            return True
        
        return dfs(0, -1) and len(visited) == n
        