class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #try to build a sequence 
        num_set = set(nums)
        #{2,20,4,10,3,5}
        longest_seq = 0
        for num in nums:
            if num-1 not in num_set:
                curr_seq = 0
                curr_num = num

                while curr_num in num_set:
                    curr_seq += 1
                    longest_seq = max(curr_seq, longest_seq)
                    curr_num += 1
            
            
        return longest_seq

        