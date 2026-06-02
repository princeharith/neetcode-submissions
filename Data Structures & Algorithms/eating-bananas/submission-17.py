class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #right_bound, max of piles
        #left_bound, 0

        #find our k (in between the bounds)
        #go through and simulate eating the bananas

        right_bound = max(piles)
        left_bound = 1
        least_hours = float('inf')
        # k = max(piles)
        k = 0

        while left_bound <= right_bound:
            num_hours = 0
            eating_rate = (right_bound+left_bound)//2
            for pile in piles:
                hours_for_this_pile = math.ceil(pile / eating_rate)
                num_hours += hours_for_this_pile

            if num_hours <= h:
                k = eating_rate
                right_bound = eating_rate-1
            else:
                left_bound = eating_rate+1
        
        return k
            


