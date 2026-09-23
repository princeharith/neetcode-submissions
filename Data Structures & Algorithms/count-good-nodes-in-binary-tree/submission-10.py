# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, greatest_in_path):
        
            if not node:
                return 0

            res = 0
            if node.val >= greatest_in_path:
                res = 1
                greatest_in_path = node.val
            
            left = dfs(node.left, greatest_in_path)
            right = dfs(node.right, greatest_in_path)
            res += (left+right)
            return res
        
        return dfs(root, root.val)
        
            
            
        