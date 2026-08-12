class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums = [1,2,2,3,3,3], k = 2

        #{1:1, 2:2, 3:3}
        counts = Counter(nums) 
        
        #[(-3, 3), (-2,2), (-1, 1)]
        max_heap = [(-cnt,num) for num,cnt in counts.items()]
        heapq.heapify(max_heap)

        res = []
        for _ in range(k):
            cnt, num = heapq.heappop(max_heap)
            res.append(num)
        
        return res
        