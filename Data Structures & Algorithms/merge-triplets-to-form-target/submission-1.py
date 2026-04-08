class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        clean_trips = []
        for trip in triplets:
            valid_trip = True
            for i in range(len(trip)):
                if trip[i] > target[i]:
                    valid_trip = False
            if valid_trip:
                clean_trips.append(trip)
        
        print(clean_trips)
        
        res = [False, False, False]
        for trip in clean_trips:
            for i in range(len(trip)):
                if not res[i] and trip[i] == target[i]:
                    res[i] = True
        
        return all(res)



                    