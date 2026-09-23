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

        good_nodes = 0
        def dfs(node, greatest_in_path):
            nonlocal good_nodes
            if not node:
                return

            if node.val >= greatest_in_path:
                good_nodes += 1
                greatest_in_path = node.val
            
            left = dfs(node.left, greatest_in_path)
            right = dfs(node.right, greatest_in_path)
        
        dfs(root, root.val)
        return good_nodes
            
            
        