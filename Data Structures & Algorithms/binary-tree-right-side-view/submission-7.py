# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        res = []

        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            level = []
            for i in range(q_len):
                node = q.popleft()

                if node:
                    print(node.val)
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                print(level)
                res.append(level[-1])
        
        return res

