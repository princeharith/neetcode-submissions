class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]

        # r = [48,24,6,1]

        # l = [1,1,2,8]

        left = [1] * len(nums)

        product = 1
        for i in range(1, len(nums)):
            left[i] = product * nums[i-1]
            product = left[i]
        
        right = [1] * len(nums)
        product = 1
        for j in range(len(nums)-2, -1, -1):
            right[j] = product * nums[j+1]
            product = right[j]

        res = []
        for i in range(len(right)):
            res.append(right[i]*left[i])
        
        return res


        