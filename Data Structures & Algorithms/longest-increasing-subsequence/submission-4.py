class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(index, prev_element_taken):
            if index == len(nums):
                return 0
            take = None
            if nums[index] > prev_element_taken:
                take = dfs(index+1, nums[index]) + 1
            skip = dfs(index+1, prev_element_taken)

            if take:
                return max(take, skip)
            else: 
                return skip
        
        return dfs(0, float('-inf'))
        