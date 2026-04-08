class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [2,-3,4,-2,2,1,-1,4]

        # curr_subarray = 2
        
        # i = 1
        # num = -3
        # #do we take -3, or -1
        # #-1

        # i=2
        # num = 4
        # #do we take 3 or 4?
        # #pick num, continue

        curr_subarray = max_subarray = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            if num > curr_subarray + num:
                curr_subarray = num
            else:
                curr_subarray += num

            max_subarray = max(curr_subarray, max_subarray)

        return max_subarray      