class Solution:
    def climbStairs(self, n: int) -> int:
        #1 = 1 -> 1
        #2 = 1,1 or 2 -> 2
        #3 = 1,1,1 or 1,2 or 2,1 -> 3
        #4 = 1,1,1,1, 2,2, 1,2,1, 2,1,1, 1,1,2
        if n == 0:
            return 0 
        if n == 1:
            return 1

        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        