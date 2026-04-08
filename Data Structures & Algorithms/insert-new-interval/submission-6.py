class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0] :
            res.append(intervals[i])
            i += 1
            
        #start point before the current's end
        while (i < n) and (newInterval[0] <= intervals[i][1]) and (newInterval[1] >= intervals[i][0]):
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])
            newInterval = [start, end]
            i += 1
        
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res


