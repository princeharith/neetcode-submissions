class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(index):
            if index == len(cost):
                return 0
            elif index > len(cost):
                #invalid
                return float('inf')
            
            if index in cache:
                return cache[index]
            
            jump_one = dfs(index+1) + cost[index]
            jump_two = dfs(index+2) + cost[index]

            cache[index] = min(jump_one, jump_two)

            return cache[index]
    

        return min(dfs(0), dfs(1))