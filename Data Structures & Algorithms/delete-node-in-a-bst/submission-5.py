# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #if the key is smaller than the curr node, we go left
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        #if the key is bigger than the curr node, we go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            #key matches, perform the delete
            #we either pick the max of the left to replace, or min of the right
            #lets pick the min of the right
            curr = root.right
            #replace root val here
            while curr.left:
                curr = curr.left
            #we have found the value!
            root.val = curr.val
            #now we delete this duplicated node...
            root.right = self.deleteNode(root.right, curr.val)
            
        
        return root

