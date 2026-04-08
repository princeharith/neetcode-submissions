class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_seen = float('-inf')
        curr = float('-inf')
        for i in range(len(nums)):
            if curr + nums[i] >= nums[i]:
                curr += nums[i]
            else:
                curr = nums[i]
            max_seen = max(curr, max_seen)
        
        return max_seen