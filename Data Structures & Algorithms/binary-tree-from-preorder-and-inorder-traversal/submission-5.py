# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        self.preIdx = 0

        def dfs(l, r):
            if l > r:
                return None

            node_val = preorder[self.preIdx]
            index = inorder_map[node_val]

            node = TreeNode(node_val)

            self.preIdx += 1

            node.left = dfs(l, index-1)
            node.right = dfs(index+1, r)

            return node
        
        return dfs(0, len(inorder)-1)