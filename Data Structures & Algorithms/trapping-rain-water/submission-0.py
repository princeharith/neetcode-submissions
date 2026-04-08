class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height)-1
        maxLeft, maxRight = height[l], height[r]
        
        res = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxLeft = max(maxLeft, height[l])
                max_water_trapped_here = (maxLeft - height[l])
                res += max_water_trapped_here
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                max_water_trapped_here = (maxRight - height[r])
                res += max_water_trapped_here
            
        return res


        