class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)


        for i in range(1, len(dp)):
            if i in coins:
                dp[i] = 1
            else:
                min_combo = float('inf')
                print(i)
                for j in range(1,(i//2)+1):
                    min_combo = min(dp[j]+dp[i-j], min_combo)
        
                dp[i] = min_combo
        return -1 if dp[-1] == float('inf') else dp[-1]

    
    




        