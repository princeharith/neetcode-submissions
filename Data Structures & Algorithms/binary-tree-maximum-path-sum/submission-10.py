# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #global variable to keep track of maxPath
        #at each node, do we include the child val or discard and use only self
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            curr_sum = node.val

            max_sum = max(max_sum, curr_sum+left+right)
            
            return curr_sum + max(left, right)
        
        dfs(root)
        return max_sum
        