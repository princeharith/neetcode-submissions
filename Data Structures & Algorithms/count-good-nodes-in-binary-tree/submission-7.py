# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #need a greatest value in path to be passed down
        #if the curr node is greater, goodNodes += 1, set new max

        def dfs(node, greatest):
            if not node:
                return 0
            
            if node.val >= greatest:
                greatest = node.val
                return 1 + dfs(node.left, greatest) + dfs(node.right, greatest)
            else:
                return dfs(node.left, greatest) + dfs(node.right, greatest)
        
        return dfs(root, float('-inf'))
        
        # dfs(root)
        # node = 2
        # greatest = 2
        # return 1 + 1 + dfs(right)
        #     dfs(left)
        #     node = 1
        #     greatest = 2
        #     return 1 + 0
        #         dfs(left)
        #         node = 3
        #         greatest = 2
        #         return 1
        #             dfs(left)
        #             node = None
        #             return 0
            
        