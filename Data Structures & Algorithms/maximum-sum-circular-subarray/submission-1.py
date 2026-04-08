class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #keep track of global max and min
        currMax, currMin = nums[0], nums[0]
        globMax, globMin = nums[0], nums[0]
        total = nums[0]

        for num in nums[1:]:
            currMax = max(num, currMax+num)
            currMin = min(num, currMin+num)

            total += num

            globMax = max(currMax, globMax)
            globMin = min(currMin, globMin)

        
        return max(globMax, total-globMin) if globMax > 0 else globMax