class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_seen = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            if (curr_max + nums[i]) > nums[i]:
                curr_max += nums[i]
            else:
                curr_max = nums[i]
            max_seen = max(max_seen, curr_max)
        
        return max_seen
