class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ''
        
        time_arr = [time for time, _ in self.hashmap[key]]  
        print(time_arr)

        l, r = 0, len(time_arr)-1
        most_recent = float('inf')
        while l <= r:
            m = (l+r)//2
            if time_arr[m] <= timestamp:
                #candidate
                most_recent = m
                l = m + 1
            else:
                r = m - 1
        if most_recent == float('inf'):
            return ''
        return self.hashmap[key][most_recent][1]


        
