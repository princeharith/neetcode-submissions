# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.lca = None
        def dfs(node, p, q):
            if not node:
                return False
            if node.val == p.val or node.val == q.val:
                self.lca = node
                return True
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and right:
                self.lca = node
                return True
            if left or right:
                return True

        dfs(root, p, q)
        return self.lca

        # def dfs(node, p, q):
        #     if not node or not p or not q:
        #         return None
        #     if max(p.val, q.val) < node.val:
        #         return dfs(node.left, p, q)
        #     elif min(p.val, q.val) > node.val:
        #         return dfs(node.right, p, q)
        #     else:
        #         return node
        
        # return dfs(root, p, q)
        