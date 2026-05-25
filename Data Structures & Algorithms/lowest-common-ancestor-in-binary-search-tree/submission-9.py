# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node, p, q):
            if not node or not p or not q:
                return None
            elif node.val < min(p.val, q.val):
                return dfs(node.right, p, q)
            elif node.val > max(p.val, q.val):
                return dfs(node.left, p, q)
            else:
                return node
        
        return dfs(root, p, q)

        
        # self.lca = root
        # def dfs(node, p, q):
        #     if not node:
        #         return
        #     if node.val == p.val:
        #         self.lca = node
        #         return True
        #     if node.val == q.val:
        #         self.lca = node
        #         return True
            
        #     left = dfs(node.left, p, q)
        #     right = dfs(node.right, p, q)

        #     if left and right:
        #         self.lca = node
            
        #     if left or right:
        #         return True
            
        
        # dfs(root, p, q)
        # return self.lca

            
        #if p and q found, return the current node