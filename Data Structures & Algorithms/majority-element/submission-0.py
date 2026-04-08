class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)

        max_v = 0
        max_k = 0
        for k,v in counts.items():
            if v > max_v:
                max_v = v
                max_k = k

        
        return max_k



        