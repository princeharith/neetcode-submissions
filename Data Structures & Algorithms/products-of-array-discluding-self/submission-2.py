class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_right = [0] * len(nums)
        to_left = [0] * len(nums)

        to_right[-1] = to_left[0] = 1
        
        for i in range(len(nums)-2, -1, -1):
            to_right[i] = nums[i+1] * to_right[i+1]
        
        for i in range(1, len(nums)):
            to_left[i] = to_left[i-1] * nums[i-1]
        
        res = []
        for i in range(len(to_left)):
            res.append(to_left[i] * to_right[i])
        
        return res

