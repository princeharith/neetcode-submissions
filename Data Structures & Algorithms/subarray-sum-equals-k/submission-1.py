class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #expected_res
        # [2], [2,-1,1], [-1,1,2], [2]

        # #input
        # [2,-1,1,2]
        # #prefixes
        # [2,1,2,4]
        # k = 2

        # res = 3

        # hashmap = {
        #     0: 3
        #     2: 2
        #     1: 1
        #     4: 1

        # }

        hashmap = defaultdict(int)
        hashmap[0] = 1
        res = 0
        running_prefix = 0

        for num in nums:
            running_prefix += num
            if running_prefix - k in hashmap:
                res += hashmap[running_prefix-k]
            
            hashmap[running_prefix] += 1
            
        return res




        