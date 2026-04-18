class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        #  l=1
        #  r=1
        #  m=1
        #  m = 1//2 = 0
        # [-1,0,2,4,6,8]
        #     r  
        #     l  


        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1