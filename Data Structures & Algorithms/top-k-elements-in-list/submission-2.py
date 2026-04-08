class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict

        num_counts = Counter(nums)

        buckets = [[] for i in range(len(nums)+1)]
        #buckets = {}
        #for i in range(len(nums)):
        #    buckets[i] = []


        
        for key, val in num_counts.items():
            buckets[val].append(key)


        res_list = []

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res_list.append(num)
                if len(res_list) == k:
                    return res_list

        
        
   