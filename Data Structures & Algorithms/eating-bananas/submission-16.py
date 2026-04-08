class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #search area of k is between 1 and max(piles)
        #select diff k's

        l, r = 1, max(piles)
        min_k = float('inf')

        #first iteration -> l = 0, r = 4
        #mid = (4)//2 = 2
        while l <= r:
            k = (l+r)//2
            hours_elapsed = 0
            for p in piles:
                hours_elapsed += math.ceil(p/k)
            if hours_elapsed <= h:
                #valid candidate, decrease k
                min_k = min(k, min_k)
                r = k - 1
            else:
                l = k + 1
        
        return min_k

            

        