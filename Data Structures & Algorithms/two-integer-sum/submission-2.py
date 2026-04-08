class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3, 4, 5, 6]
        # target = 7
        # what we're looking for {4: 0, 3: 1, 2: 2, 1: 3}
        #return with smaller index first

        #map so we can save the index also
        #except the key is gonna be the number to look for, and 
        #val is gonna be the index
        target_map = {}

        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if nums[i] in target_map:
                return [target_map[nums[i]], i]
            target_map[num_to_find] = i
        



        