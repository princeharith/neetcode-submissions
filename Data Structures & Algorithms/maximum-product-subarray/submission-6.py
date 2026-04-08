class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_arr = [1] * (len(nums))
        max_arr = [1] * (len(nums))
        min_arr[0] = max_arr[0] = nums[0]

        for i in range(1, len(nums)):
            max_arr[i] = max(nums[i], nums[i]*max_arr[i-1], nums[i]*min_arr[i-1])
            min_arr[i] = min(nums[i], nums[i]*max_arr[i-1], nums[i]*min_arr[i-1])
        print(max_arr)
        print(min_arr)
        return max(max_arr)
    #     [1,2,-3,4]
    #     max(nums[i-1] * max[i] or nums[i-1] * min[i])
    #        |
    #       \ /
    # max=[1,1,2,-3,4]
    # min=[1,1,2,-6,-24]

    #     [-2,-1]
    # max=[-2,]
    # min=[-2,]