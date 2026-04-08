class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num-1 not in num_set:
                curr_streak = 0
                while num + curr_streak in num_set:
                    curr_streak += 1
                    longest_streak = max(curr_streak, longest_streak)

        
        return longest_streak
        