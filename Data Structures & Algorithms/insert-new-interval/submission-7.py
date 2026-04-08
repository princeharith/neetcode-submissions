class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []
        n = len(intervals)

        #currInterval ends before new starts
        while i < n and intervals[i][1] < newInterval[0] :
            res.append(intervals[i])
            i += 1
            
        #we want to loop until 
        while (i < n) and intervals[i][0] <= newInterval[1]:
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])
            newInterval = [start, end]
            i += 1
        
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res


