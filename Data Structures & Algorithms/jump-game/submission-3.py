class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums)-1
        arr = [False] * len(nums)
        arr[-1] = True

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_idx:
                arr[i] = True
                last_idx = i
        
        return arr[0]
