class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(index, canBuy):
            if index >= len(prices):
                return 0
            
            if (canBuy, index) in cache:
                return cache[(canBuy, index)]

            #do nothing
            cooldown = dfs(index+1, canBuy)
            #buy
            if canBuy:
                buy = dfs(index+1, not canBuy)-prices[index]
                cache[(canBuy, index)] = max(cooldown, buy)
            
            #sell
            else:
                sell = dfs(index+2, not canBuy)+prices[index]
                cache[(canBuy, index)] = max(cooldown, sell)
            
            return cache[(canBuy, index)]

        dfs(0,True)
        return cache[(True, 0)]