class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_counter = collections.Counter(nums)
        
        for k,v in collections.Counter(nums).items():
            if v >= 2:
                return k
        