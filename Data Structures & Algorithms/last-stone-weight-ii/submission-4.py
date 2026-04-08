class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        targetSum = sum(stones) // 2
        memo = {}

        def backtrack(currSum, i):
            if (currSum, i) in memo:
                return memo[(currSum, i)]
            if i == len(stones) or currSum >= targetSum:
                return abs(currSum - (sum(stones) - currSum))
            
            memo[(currSum, i)] = min(backtrack(currSum+stones[i], i+1), backtrack(currSum, i+1))
            return memo[(currSum, i)]
        
        return backtrack(0, 0)
        