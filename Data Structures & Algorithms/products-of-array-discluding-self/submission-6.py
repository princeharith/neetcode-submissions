class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [1] * len(nums)
        for i in range(1, len(nums)):
            product_left[i] = product_left[i-1] * nums[i-1]
        
        product_right = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            product_right[i] = product_right[i+1] * nums[i+1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = product_left[i] * product_right[i]
        
        return res
        