class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target_subset_sum = sum(nums) // 2

        # [1,2,3,4]
        memo = {}

        def backtrack(index, curr_sum):
            if (index, curr_sum) in memo:
                return memo[(index,curr_sum)]
            if curr_sum == target_subset_sum:
                return True
            if curr_sum > target_subset_sum or index >= len(nums):
                return False
            
            #either take the current elemene or dont
            memo[(index, curr_sum)] = backtrack(index+1, curr_sum+nums[index]) or backtrack(index+1, curr_sum)

            return memo[(index, curr_sum)]

        return backtrack(0, 0)