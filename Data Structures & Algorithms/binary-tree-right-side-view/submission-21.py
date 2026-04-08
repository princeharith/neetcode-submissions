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
            rightSide = None
            q_len = len(q)
            print(q)
            for _ in range(q_len):
                node = q.popleft()
                if node:
                    q.append(node.left) 
                    q.append(node.right)
                    rightSide = node.val
            if rightSide:
                res.append(rightSide)
        
        return res


        