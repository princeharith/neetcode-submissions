class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get the counts
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        #buckets = [[], [1], [2], [3], [], [], []]

        #bucketing, each index in my list of buckets represents frequency of element
        for key,val in counts.items():
            buckets[val].append(key)

        res = []
        #loop backwards, append to res and keep checking k
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        