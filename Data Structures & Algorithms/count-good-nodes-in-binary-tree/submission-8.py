# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, greatest_in_path):
            if not node:
                return 0
            if node.val >= greatest_in_path:
                left = dfs(node.left, node.val)
                right = dfs(node.right, node.val)
                return 1 + left + right
            else:
                return dfs(node.left, greatest_in_path) + dfs(node.right, greatest_in_path)
        
        return dfs(root, root.val)

    

            
            
            

        