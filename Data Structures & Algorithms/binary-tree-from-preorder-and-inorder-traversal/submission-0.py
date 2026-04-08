# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #build a dict mapping the 
        indices_dict = {val: idx for idx, val in enumerate(inorder)}

        self.preIdx = 0

        def dfs(l,r):
            if l > r:
                return None

            root_val = preorder[self.preIdx]
            self.preIdx += 1

            partition = indices_dict[root_val]
            root = TreeNode(root_val)
            
            root.left = dfs(l, partition-1)
            root.right = dfs(partition+1, r)

            return root
        
        return dfs(0, len(inorder)-1)

            