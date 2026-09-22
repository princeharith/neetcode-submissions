class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(i, curr_sum, curr_list):
            if curr_sum == target:
                res.append(curr_list.copy())
                return
            elif i == len(nums) or curr_sum > target:
                return
            
            for j in range(i, len(nums)):
                if curr_sum + nums[j] > target:
                    return
                curr_list.append(nums[j])
                backtrack(j, curr_sum+nums[j], curr_list)
                curr_list.pop()
                
                # backtrack(i+1, curr_sum, curr_list)
        
        backtrack(0, 0, [])
        return res

        