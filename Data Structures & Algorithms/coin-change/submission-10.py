class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
    
        dp = [float('inf') for _ in range(amount+1)]

        for amt in range(1, amount+1):
            for coin in coins:
                if amt - coin == 0:
                    dp[amt] = 1
                elif amt - coin > 0:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        
        return -1 if dp[-1] == float('inf') else dp[-1]


