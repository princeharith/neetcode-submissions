class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #nums = [1,2,4,6]
        
        [48,24,6,1]
        #res =  [48,24,12,8]

        left = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        #left = [1,1,2,8]
        right = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res
         


        