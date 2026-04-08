class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #    target = 7
    #     nums = [3,4,5,6]
    #    to_find={3:0, }

        to_find = {}
        for i,num in enumerate(nums):
            if target-num in to_find:
                return [to_find[target-num], i]
            to_find[num] = i




