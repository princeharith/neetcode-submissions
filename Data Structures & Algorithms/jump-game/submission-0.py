class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        goal_index = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal_index:
                goal_index = i
            
        return True if goal_index == 0 else False

        