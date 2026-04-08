# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #[1] -> pop [] -> append children [2, 3]
        q = collections.deque()

        if not root:
            return []

        q.append(root)
        res = []

        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left) 
                    if node.right:
                        q.append(node.right)
                    rightSide = node.val
            res.append(rightSide)
        
        return res


        