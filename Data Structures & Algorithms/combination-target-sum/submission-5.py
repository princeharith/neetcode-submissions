class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        def backtrack(i, curr_sum, curr_list):
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            elif i == len(nums) or curr_sum > target:
                return

            curr_list.append(nums[i])
            backtrack(i, curr_sum+nums[i], curr_list)
            curr_list.pop()
            backtrack(i+1, curr_sum, curr_list)
        
        backtrack(0, 0, [])
        return res

        