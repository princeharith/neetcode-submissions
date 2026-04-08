# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            q_len = len(q)
            curr_level = []
            print(q)
            for _ in range(q_len):
                node = q.popleft()
                curr_level.append(node.val)

                
                left_node, right_node = node.left, node.right
                if left_node:
                    q.append(left_node)
                if right_node:
                    q.append(right_node)
            res.append(curr_level[-1])
        
        return res
                    
        