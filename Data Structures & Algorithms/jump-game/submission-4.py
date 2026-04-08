class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i
        
        return True if last_idx == 0 else False
