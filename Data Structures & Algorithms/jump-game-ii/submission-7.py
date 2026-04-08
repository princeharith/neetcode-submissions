class Solution:
    def jump(self, nums: List[int]) -> int:

        #pick the largest jump I can (greedy)
        #After picking the largest jump, check the search area and 
        #pick the largest from there
        #We want to maximize not the biggest jump seen, but what can
        #TAKE us the farthest

        if len(nums) == 1 or len(nums) == 0:
            return 0

        i = 0
        num_jumps = 0
        while i < len(nums):
            max_jump_seen = 0
            new_j = 0

            for j in range(i+1, i+1+nums[i]):
                if j >= len(nums)-1:
                    return num_jumps + 1
                if j + nums[j] >= max_jump_seen:
                    max_jump_seen = j + nums[j]
                    new_j = j

            

            num_jumps += 1
            i = new_j
        
            


        