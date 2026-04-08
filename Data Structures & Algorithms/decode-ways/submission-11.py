class Solution:
    def numDecodings(self, s: str) -> int:

        #we do a single digit and 2 digit check

        #remember, just because we have an extra digit 
        #doesn't inherently mean we do dp[i] = dp[i+1] + 1

        #because if we have 1 vs 11, [1,1] is still only one way to decode
        #it becomes 2 ways to decode BC of it being two digis
        dp = [0] * (len(s)+1)
        dp[0] = 1
        
        for i in range(1,len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and (10 <= int(s[i-2:i]) <= 26):
                dp[i] += dp[i-2]
        
        print(dp)
        return dp[-1]



        