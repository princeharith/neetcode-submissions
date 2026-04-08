class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # max_k = max(piles)
        # k_list = [i for i in range(1, max_k+1)]

        l, r = 1, max(piles)

        min_rate = max(piles)

        while l <= r:
            mid = (l+r)//2
            k = mid
            time = 0

            for num in piles:
                time += math.ceil(float(num)/k)

            if time <= h:
                min_rate = min(min_rate, k)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_rate



