class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(index):
            if index == n:
                return 1
            elif index > n:
                return 0

            if index in cache:
                return cache[index]

            one_jump = dfs(index+1)
            two_jumps = dfs(index+2)
            
            cache[index] = one_jump + two_jumps
            return dfs(index+1) + dfs(index+2)
        
        return dfs(0)
        