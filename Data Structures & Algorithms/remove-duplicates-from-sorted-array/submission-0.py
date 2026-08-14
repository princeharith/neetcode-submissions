class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # [1,2,3,4,4]
        #          l
        #          r

        l, r = 0, 0 
        while r < len(nums):
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
            
            for _ in range(1):
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l
        