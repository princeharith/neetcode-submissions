class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in cache:
                return cache[(i, canBuy)]
            
            if canBuy:
                #profit from buying now
                buy = dp(i+1, not canBuy) - prices[i]
                cooldown = dp(i+1, canBuy)
                cache[(i, canBuy)] = max(buy, cooldown)
            else:
                sell = dp(i+2, not canBuy) + prices[i]
                cooldown = dp(i+1, canBuy)
                cache[(i, canBuy)] = max(sell, cooldown)
            
            return cache[(i, canBuy)]
        
        return dp(0, True)
        
            