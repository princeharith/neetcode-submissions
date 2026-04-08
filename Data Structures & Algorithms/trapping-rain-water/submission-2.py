class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        max_water_trapped_here = 0

        while l < r:
            maxLeft = max(height[l], maxLeft)
            maxRight = max(height[r], maxRight)
            if height[l] < maxLeft:
                max_water_trapped_here += (maxLeft - height[l])
            if height[r] < maxRight:
                max_water_trapped_here += (maxRight - height[r])
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water_trapped_here