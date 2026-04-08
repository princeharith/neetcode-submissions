class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        max_seen = nums[0]

        for i in range(1, len(nums)):
            if running_sum + nums[i] > nums[i]:
                running_sum += nums[i]
            else:
                running_sum = nums[i]
            max_seen = max(running_sum, max_seen)

        return max_seen