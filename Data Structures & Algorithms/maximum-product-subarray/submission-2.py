class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0,0] for num in nums]
        dp[0] = [nums[0], nums[0]]
        max_seen = dp[0][1]
        for i in range(1, len(nums)):
            dp[i][0] = min(nums[i]*dp[i-1][0], nums[i], nums[i]*dp[i-1][1])
            dp[i][1] = max(nums[i]*dp[i-1][0], nums[i], nums[i]*dp[i-1][1])
            max_seen = max(max_seen, dp[i][1])

        return max_seen