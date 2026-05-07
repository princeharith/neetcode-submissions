class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l,r = 0, k

        while r < len(nums)+1:
            curr_largest = float('-inf')
            for i in range(l, r):
                if nums[i] > curr_largest:
                    curr_largest = nums[i]
            res.append(curr_largest)

            l += 1
            r += 1
        
        return res