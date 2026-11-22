class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)+1
        dp = [0] * n
        dp[1] = nums[0]        

        #dp[i] is what we can rob until (not including) the ith house
        for i in range(2, n):
            dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
        
        return max(dp)