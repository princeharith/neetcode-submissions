class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        count_list = [(-cnt, num) for num, cnt in counts.items()]

        heapq.heapify(count_list)

        res = []
        for _ in range(k):
            cnt, num = heapq.heappop(count_list)
            res.append(num)
        
        return res

        
        