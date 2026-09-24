class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Counter to keep track of counts
        #when we have that, we can go through the counts (in some sorted fashion by count, decreasing)
        #append to a list, once list reaches length k, we can break and return
        
        if not nums:
            return []

        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for element, frequency in counts.items():
            buckets[frequency].append(element)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for element in buckets[i]:
                res.append(element)
                if len(res) == k:
                    return res
        
        