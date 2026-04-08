class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins))]

        #there is always a way to make amount 0 (no coins taken)
        for c in range(len(coins)):
            dp[c][0] = 1
        
        for a in range(1, amount+1):
            if a >= coins[0]:
                dp[0][a] = dp[0][a-coins[0]]
        
        for c in range(1, len(coins)):
            for a in range(1, amount+1):
                #as if we didn't use the current coin...
                dp[c][a] = dp[c-1][a]
                if a >= coins[c]:
                    dp[c][a] += dp[c][a-coins[c]]
        
        return dp[-1][-1]
