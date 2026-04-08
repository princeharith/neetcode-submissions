class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        # [1,3,5,7,9]
        #       r l 

        if nums[l] < target:
            return l + 1
        else:
            return l 