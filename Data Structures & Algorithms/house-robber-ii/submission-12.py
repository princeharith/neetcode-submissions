class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(houses):
            n = len(houses)+1
            dp = [0] * n
            dp[1] = houses[0]

            for i in range(2,n):
                dp[i] = max(dp[i-2] + houses[i-1], dp[i-1])
            
            return dp[-1]
        
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))

        