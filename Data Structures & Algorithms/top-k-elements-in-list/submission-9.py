class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        reversed_counts = defaultdict(list)

        for key,val in counts.items():
            reversed_counts[val].append(key)
        
        key_list = reversed_counts.keys()
    

        res = []
        for key in sorted(key_list, reverse=True):
            for val in reversed_counts[key]:
                if len(res) < k:
                    res.append(val)
        return res
        

        



        