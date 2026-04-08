# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        self.goodNodeList = []

        def dfs(node, max_in_path):
            if not node:
                return
            max_in_path = max(node.val, max_in_path)
            dfs(node.left, max_in_path)
            dfs(node.right, max_in_path)

            if node.val < max_in_path:
                return
            self.goodNodes += 1
            self.goodNodeList.append(node.val)
        


        dfs(root, root.val)

        print(self.goodNodeList)
        return self.goodNodes