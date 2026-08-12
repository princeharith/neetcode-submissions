class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        looking_for = dict()

        for i in range(len(nums)):
            if nums[i] in looking_for:
                return [looking_for[nums[i]], i]
            looking_for[target-nums[i]] = i