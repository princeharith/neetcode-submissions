class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        #numSet = (2,20,4,10,3,5)

        longestSeq = 0
        for num in nums:
            if num-1 not in numSet:
                #we can try to build a sequence
                curr_num = num
                #curr_num = 6
                curr_seq = 0
                #curr_seq = 4

                while curr_num in numSet:
                    curr_num += 1
                    curr_seq += 1
                longestSeq = max(curr_seq, longestSeq)
        
        return longestSeq



        