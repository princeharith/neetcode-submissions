class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1,7,2,5,4,7,3,6]
        #    p1          p2


        # length = p2 - p1 = 6
        # height = min(nums[p1], nums[p2]) = 6
        # length * height = 36
        # max_area = 36

        max_area = 0
        p1, p2 = 0, len(heights)-1

        while p1 < p2:
            length = p2-p1
            height = min(heights[p2], heights[p1])
            max_area = max(max_area, length*height)

            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return max_area

        