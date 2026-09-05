class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        #    buy
        #            sell
        if len(prices) == 1:
            return 0
        
        buy, sell = 0, 1
        maxProfit = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
                continue
            maxProfit = max(maxProfit, prices[sell]-prices[buy])
            sell += 1
        
        return maxProfit

         
        
        