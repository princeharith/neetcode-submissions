# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def lcaHelper(node, p , q):
            if not node:
                return
            print(node.val)
            if p.val <= node.val and q.val >= node.val:
                print("Reached!")
                return node
            elif p.val < node.val and q.val < node.val:
                return lcaHelper(node.left, p, q)
            else:
                return lcaHelper(node.right, p, q)
        if p.val < q.val:
            minNode = p
            maxNode = q
        else:
            minNode = q
            maxNode = p
        return lcaHelper(root, minNode, maxNode)

