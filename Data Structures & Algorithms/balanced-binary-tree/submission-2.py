# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True
        
        def dfs(node):

            if not node:
                return 0 
            
            path_left = 1 + dfs(node.left)
            path_right = 1 + dfs(node.right)

            if abs(path_left - path_right) > 1:
                nonlocal isBalanced
                isBalanced = False
            return max(path_left, path_right)

        dfs(root)
        return isBalanced

                




            
        