class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(index, running_sum):
            if index == len(nums):
                if running_sum == target:
                    return 1
                else:
                    return 0
                
            if (index, running_sum) in cache:
                return cache[(index, running_sum)]
            
            add = dfs(index+1, running_sum+nums[index])
            sub = dfs(index+1, running_sum-nums[index])
            
            cache[(index, running_sum)] = add + sub
            
            return add + sub

        dfs(0,0)
        return cache[(0,0)]
        