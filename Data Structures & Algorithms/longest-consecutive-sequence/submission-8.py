class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #when do we actually want to loop through the set? 

        #numSet = {1,2,3, 39,38,37,36}
        #curr_seq = 4
        #curr_num = 40

        numSet = set(nums)
        longest_seq = 0

        for num in nums:
            #beginning of a sequence...
            if num - 1 not in numSet:
                curr_seq = 0
                curr_num = num

                while curr_num in numSet:
                    curr_seq += 1
                    curr_num += 1
                    longest_seq = max(longest_seq, curr_seq)
        
        return longest_seq

        










