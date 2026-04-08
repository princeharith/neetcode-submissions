# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #mapping inorder values to indices
        inorder_map = {val:idx for idx, val in enumerate(inorder)}
        preIdx = 0

        def buildSubtree(l,r):
            nonlocal preIdx
            if l > r:
                return None
            curr_root = preorder[preIdx]
            root_idx = inorder_map[curr_root]

            root = TreeNode(val=curr_root)

            preIdx += 1
            
            if l == r:
                return root

            
            root.left = buildSubtree(l, root_idx-1)
            root.right = buildSubtree(root_idx+1, r)

            return root
        
        return buildSubtree(0, len(preorder)-1)

        

        