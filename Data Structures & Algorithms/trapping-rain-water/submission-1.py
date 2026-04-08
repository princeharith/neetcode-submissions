class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        max_water_trapped_here = 0

        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                max_water_trapped_here += (maxLeft - height[l])
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                max_water_trapped_here += (maxRight - height[r])
                r -= 1
        
        return max_water_trapped_here


        