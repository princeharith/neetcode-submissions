# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, left_constraint, right_constraint):
            if not node:
                return True
            
            left = dfs(node.left, left_constraint, node.val)
            right = dfs(node.right, node.val, right_constraint)

            if left_constraint < node.val < right_constraint:
               return left and right
            
            return False
        
        
        return dfs(root, float('-inf'), float('inf'))

        




        