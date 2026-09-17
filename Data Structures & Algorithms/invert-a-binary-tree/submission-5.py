# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def dfs(node):
        #     if not node:
        #         return 
        #     node.left, node.right = node.right, node.left
        #     dfs(node.left)
        #     dfs(node.right)
        
        # dfs(root)
        # return root

    #     1 
    #   3    2
        if not root:
            return None
        def bfs(node):
            q = deque()
            q.append(node)
            #q = 3, 4, 5
            while q:
                curr = q.popleft()
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
        bfs(root)
        return root
                 


        