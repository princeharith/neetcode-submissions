class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights)-1

        while l < r:
            width = r-l
            height = min(heights[l], heights[r])
            max_area = max(max_area, width*height)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
        #area = h * w
        # where the h is the smalles of the 2 bars
        # where w is the distance between
        # return the max amount of water

        # we want to maximize the distance b/w two bars,
        #and then check for height

        #we want to keep the bigger height, so compare 
        #heights[l], heights[r] and increment one

        #[1,7,2,5,4,7,3,6]
        #   *         *  
        
    

        #w = r-l = 7-0 = 5
        #h = min(heights[l], heights[r]) = 3

        15

        #area = 7


        