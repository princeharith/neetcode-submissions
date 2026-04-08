class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        reverse_count = defaultdict(list)
        
        for key,val in count.items():
            reverse_count[val].append(key)
        
        sorted_counts = sorted(reverse_count.keys(), reverse=True)

        print(reverse_count)

        res = []
        for key in sorted_counts:
            for num in reverse_count[key]:
                res.append(num)
                if len(res) == k:
                    print("HELLO")
                    return res

        