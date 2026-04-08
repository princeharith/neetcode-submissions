class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        n = len(nums)
        target = total // 2
        
        dp = [[False] * (target+1) for _ in range(n+1)]
        
        for i in range(n):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i-1] <= target:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[i][target]
                