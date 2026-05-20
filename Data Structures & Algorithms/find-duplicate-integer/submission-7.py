class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        for i, num in enumerate(nums):
            if nums[abs(num)-1] < 1:
                return abs(num)
            nums[abs(num)-1] *= -1
        

        

        