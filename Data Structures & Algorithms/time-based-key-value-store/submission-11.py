class TimeMap:

    #alice: [(1, 'happy'), ()]

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        #find the timestamp, return the one before it?
        vals = self.time_map.get(key)
        if not vals:
            return ""

        l, r = 0, len(vals)-1
        candidate = ""
        while l <= r:
            mid = (l+r)//2
            if vals[mid][0] <= timestamp:
                candidate = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return candidate




         
        
        
