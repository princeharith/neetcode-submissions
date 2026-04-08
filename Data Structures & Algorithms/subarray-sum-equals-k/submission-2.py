class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

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




        