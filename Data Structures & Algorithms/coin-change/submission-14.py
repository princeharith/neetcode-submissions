class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        #amount = 5
        #coins = [1,2,5]
        #[0, 1, 1, 3, 2, 1]
                    #2 at index 3 because we need 1 and 2
                    #2 at index 4 bc we can do 2 and 2
                    #

        for amount in range(1, len(dp)):
            for c in coins:
                if amount - c == 0:
                    dp[amount] = 1
                elif amount - c > 0:
                    dp[amount] = min(dp[amount-c] + 1, dp[amount])
        
        #[inf, inf, inf]
        
        return -1 if dp[amount] == float('inf') else dp[amount]



