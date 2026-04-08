class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #keep track of max and min, products are a but more interesting
        dpMin = [0]*len(nums)
        dpMax = [0]*len(nums)

        maxSeen = dpMin[0] = dpMax[0] = nums[0]

        for i in range(1, len(nums)):
            dpMin[i] = min(dpMin[i-1]*nums[i], nums[i], dpMax[i-1]*nums[i])
            dpMax[i] = max(dpMin[i-1]*nums[i], nums[i], dpMax[i-1]*nums[i])
            maxSeen = max(dpMax[i], maxSeen)
        
        return maxSeen

     
        
        