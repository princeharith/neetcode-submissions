class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list)
        #self.hashmap = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        vals = self.hashmap[key]

        if timestamp < vals[0][1]:
            return ""

        l, r = 0, len(vals)-1
        while l <= r:
            mid = (l + r) // 2
            if vals[mid][1] == timestamp:
                return vals[mid][0]
            elif vals[mid][1] < timestamp:
                l = mid + 1
            else: 
                r = mid - 1
        return vals[r][0]
        
        
