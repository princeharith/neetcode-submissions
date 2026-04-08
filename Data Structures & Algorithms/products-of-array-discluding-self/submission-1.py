class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        allMultiplied = 1
        foundZero = False
        num_zeros = 0

        for num in nums:
            if num == 0:
                foundZero = True
                num_zeros += 1
                continue
            allMultiplied *= num
        
        if num_zeros > 1:
            return [0] * len(nums)
        
        res = []
        for num in nums:
            if foundZero and num == 0:
                res.append(allMultiplied)
            elif foundZero and num != 0:
                res.append(0)
            else:
                res.append(allMultiplied // num)
        return res