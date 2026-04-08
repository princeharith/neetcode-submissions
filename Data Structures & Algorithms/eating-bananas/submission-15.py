class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #find rate K
        #return min rate
        #you have h hours

        #what k am I guarn't to eat all banannas?
        #max of pile

        #k = 4, finish in 4 hours

        #confused with the loop - do I loop thru each bannana? 
        #How do I know how to change k?
        l,r = 1, max(piles)
        min_k = max(piles)
        while l <= r:
            mid = (l+r)//2
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile/mid)
            if curr_h <= h:
                min_k = min(min_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_k


