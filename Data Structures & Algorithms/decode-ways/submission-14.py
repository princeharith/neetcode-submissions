class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        # 1012
        n = len(s)+1
        dp = [0] * n

        dp[0] = 1
        dp[1] = 1

        #dp = [1,1,1,1,12]

        for i in range(2, n):
            dp[i] += dp[i-1] if s[i-1] != '0' else 0
            dp[i] += dp[i-2] if 10 <= int(s[i-2:i]) <= 26 else 0
        
        return dp[n-1]



        