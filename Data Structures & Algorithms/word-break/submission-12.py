class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)+1
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[-1]
        