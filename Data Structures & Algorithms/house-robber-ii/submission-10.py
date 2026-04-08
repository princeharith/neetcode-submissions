class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        def dfs(index, modified_nums):
            if index >= len(modified_nums):
                return 0
            
            if index in cache:
                return cache[index]
            
            #rob this house
            rob = dfs(index+2,modified_nums)+modified_nums[index]
            dont_rob = dfs(index+1, modified_nums)

            cache[index] = max(rob,dont_rob)

            return max(rob, dont_rob)
        
        cache = {}
        rob_last_house = dfs(0, nums[1:])

        cache = {}
        rob_first_house = dfs(0, nums[:-1])

        return max(rob_first_house, rob_last_house)
        