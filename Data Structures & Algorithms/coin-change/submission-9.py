class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        coins = set(coins)

        if amount == 0:
            return 0

        for amount in range(1, len(dp)):
            if amount in coins:
                dp[amount] = 1
                continue
            for c in coins:
                if amount - c >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount-c])
        print(dp)
        return dp[-1] if dp[-1] != (amount+1) else -1
