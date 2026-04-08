class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(index, curr_amount):
            if curr_amount == amount:
                    return 0
                    
            if index == len(coins) or curr_amount > amount:
                return float('inf')
            
            if (index, curr_amount) in cache:
                return cache[(index, curr_amount)]
            
            take = dfs(index, curr_amount+coins[index])+1
            skip = dfs(index+1, curr_amount)
            
            cache[(index, curr_amount)] = min(take, skip)
            return cache[(index, curr_amount)]

        res = dfs(0,0)
        if res == float('inf'):
            return -1
        else:
            return res