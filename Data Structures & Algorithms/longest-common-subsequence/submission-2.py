class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #for the empty string
        ROWS, COLS = len(text1)+1, len(text2)+1

        dp = [[0] * COLS for _ in range(ROWS)]

        for i in range(1,ROWS):
            for j in range(1,COLS):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]