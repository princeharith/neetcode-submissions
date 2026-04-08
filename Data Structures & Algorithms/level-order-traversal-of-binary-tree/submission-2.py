# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            curr_level = []
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    curr_level.append(node.val)
                    left,right = node.left, node.right
                    q.append(left)
                    q.append(right)
            if curr_level:
                res.append(curr_level)
        return res


