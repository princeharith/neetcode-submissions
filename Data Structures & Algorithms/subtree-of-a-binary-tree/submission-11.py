# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #go through the root
            #if curr root == subroot, check the subtree
        
        #if we run out of root, return False
        if not root:
            return False

        def dfs(curr, subRoot):
            if not curr and not subRoot:
                return True
            if not curr or not subRoot:
                return False
            return curr.val == subRoot.val and dfs(curr.left, subRoot.left) and dfs(curr.right, subRoot.right)
        
        if root.val == subRoot.val:
            if dfs(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        