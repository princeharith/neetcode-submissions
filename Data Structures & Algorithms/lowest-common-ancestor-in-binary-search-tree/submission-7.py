# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, p, q):
            if not node:
                return None
            
            if node.val == p.val:
                return node
            
            if node.val == q.val:
                return node
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and right:
                return node
            return left or right
        
        return dfs(root, p, q)