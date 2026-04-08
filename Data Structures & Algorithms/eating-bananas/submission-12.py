class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = max(piles)
        
        while l <= r:
            k = (l+r)//2
            
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/k)
            
            if hours_spent <= h:
                r = k - 1
                min_k = min(k, min_k)
            else:
                l = k + 1
        
        return min_k



