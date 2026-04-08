class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
                r+=1
            else:
                profit = max(profit, prices[r]-prices[l])
                r += 1
        return profit
            



        #[10, 1, 5, 6, 7, 1]
        #      *  *  

        #5-1 = 4


        #choose not to sell, profit is 0
        #hence we don't want any negative profits

        #if r pointer > l pointer, we buy at l pointer
        #else, we traverse
        
        #buy low, sell high
        #if the 
        