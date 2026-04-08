class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        #l<r since we want it to break once they meet
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                #smallest element, or pivot at right side of array
                l = m + 1
            else:
                r = m
        
        return nums[r]
        