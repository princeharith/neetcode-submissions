class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_counter = collections.Counter(nums)
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i])-1] *= -1

        print(nums) 