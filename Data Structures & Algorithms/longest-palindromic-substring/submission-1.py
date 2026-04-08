class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        #i, j in the above will represent if s[i:j+1] is a palindrome
        residx, resLen = 0,0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if (j-i+1) > resLen:
                        resLen = (j-i+1)
                        residx = i
    
        return s[residx:residx+resLen]
        