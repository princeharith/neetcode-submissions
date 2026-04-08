class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #res depends on the suffix
        #suffix depends on the num

        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
