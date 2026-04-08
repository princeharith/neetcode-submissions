class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i] means, can s[:i-1] be segmented?
        dp = [False] * (len(s)+1)
        #empty string can be segmented
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        print(dp)
        return dp[-1]
        