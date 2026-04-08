class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #either want to take a coin, or not take a coin

        dp = [[0]*(amount+1) for _ in range(len(coins))]

        for c in range(len(coins)):
            #can always make amount=0, for every coin
            dp[c][0] = 1
        
        #for first row
        for a in range(1, amount+1):
            #see if we can take the coin
            if a >= coins[0]:
                dp[0][a] = dp[0][a-coins[0]]
        
        for c in range(1, len(coins)):
            for a in range(1, amount+1):
                #skip the coin:
                dp[c][a] = dp[c-1][a]

                if amount >= coins[c]:
                    #if we take the coin, we add the number of ways we made
                    #the prev amount with the same coin
                    dp[c][a] += dp[c][a-coins[c]]
        
        return dp[-1][-1]
        

        #                    amount=0  amount=1
        # include coins[0]? 
        # include coins[1]?