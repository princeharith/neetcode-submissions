class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #we need to find the least weight capacity,
        #s.t. all packages shipped in d days

        #each day, we can load capacity w

        #binary search??
        #min capacity = 0?
        #max capacity = sum(weights) 
        #min = ??

        #we need to try different capacities

        #weights = [1,5,4,4,2,3], days = 3

        min_c, max_c = max(weights), sum(weights)
        #min_c = 5
        #max_c = 11


        

        while min_c < max_c:
            middle_c = (max_c+min_c)//2
            #middle_c = 8
            num_days = 0
            #num_days = 3

            curr_capacity = 0
            #curr_capacity = 5
            for i in range(len(weights)):
                if curr_capacity + weights[i] <= middle_c:
                    curr_capacity += weights[i]
                    continue
                num_days += 1
                curr_capacity = weights[i]
            
            num_days += 1
            
            if num_days <= days:
                max_c = middle_c
            else:
                min_c = middle_c+1
        
        return min_c
