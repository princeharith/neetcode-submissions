class Solution:
    def canJump(self, nums: List[int]) -> bool:


        goal_index = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            print('in loop')
            if i + nums[i] >= goal_index:
                goal_index = i
            
        return True if goal_index == 0 else False

        