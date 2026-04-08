# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def path(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            
            path_left = path(node.left) + 1
            path_right = path(node.right) + 1

            return max(path_left, path_right)
        
        return path(root)
        