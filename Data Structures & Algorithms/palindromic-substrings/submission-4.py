class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[False]*len(s) for _ in range(len(s))]
        print(dp)

        for i in range(len(s)-1,-1,-1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if (j-i+1 <= 2) or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        count += 1
        
        return count
        