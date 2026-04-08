"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#bfs
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToClone = {}
        initial_clone = Node(node.val, [])
        oldToClone[node] = initial_clone

        q = collections.deque()
        q.append(node)

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in oldToClone:
                    oldToClone[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)

                oldToClone[curr].neighbors.append(oldToClone[neighbor])
        
        return oldToClone[node]