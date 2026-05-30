# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #global variable to keep track of maxPath
        #at each node, do we include the child val or discard and use only self
        max_sum = float('-inf')

        def dfs(node):
            nonlocal max_sum

            if not node:
                return float('-inf')
            
            left = dfs(node.left)
            right = dfs(node.right)

            curr_sum = node.val

            print(f'the curr_sum NOW is {curr_sum}')
            max_sum = max(max_sum, curr_sum+left+right, curr_sum+left, curr_sum+right, curr_sum)
            print(f'the max_sum is {max_sum}')
            
            to_add = 0
    
            if left > right:
                to_add = left
            else:
                to_add = right
            
            curr_sum = max(curr_sum, curr_sum + to_add)



            return curr_sum
        
        dfs(root)
        return max_sum
        