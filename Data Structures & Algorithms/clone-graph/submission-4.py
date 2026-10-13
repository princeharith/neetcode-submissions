"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_copy = {}
        if not node:
            return None

        def dfs(node):
            if node in old_to_copy:
                return old_to_copy[node]
            copy = Node(node.val)
            old_to_copy[node] = copy
            for nei in node.neighbors:
                old_to_copy[node].neighbors.append(dfs(nei))
            return old_to_copy[node]
        
        dfs(node)
        return old_to_copy[node]
        