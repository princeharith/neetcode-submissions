# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            q_len = len(q)
            curr_level = []
            for _ in range(q_len):
                node = q.popleft()
                curr_level.append(node.val)
                left = node.left
                right = node.right

                if left:
                    q.append(left)
                if right:
                    q.append(right)
        
            res.append(curr_level)
        
        return res
            

        