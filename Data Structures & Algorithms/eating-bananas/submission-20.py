class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        floor = 1
        ceil = max(piles)
        k = float('inf')
        
        [25,10,23,4]

        #smallest: 25
        #potential: 25

        #what is our condition?
        while floor <= ceil:
            k_to_try = (floor + ceil)//2
            hours_elapsed = 0 
            for item in piles:
                hours_elapsed += math.ceil(item/k_to_try)
            if hours_elapsed <= h:
                k = min(k, k_to_try)
                ceil = k_to_try - 1
            else:
                floor = k_to_try + 1
        
        return k
                
            
     

