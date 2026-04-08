class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarray = max_subarray = nums[0]
        for i in range(1, len(nums)):
            curr_subarray = max(nums[i], nums[i]+curr_subarray)
            max_subarray = max(curr_subarray, max_subarray)

        return max_subarray      