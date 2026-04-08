class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newInterval = intervals[0]
        res = []
        

        for i in range(1, len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                start =  min(intervals[i][0], newInterval[0])
                end = max(intervals[i][1], newInterval[1])
                newInterval = [start, end]
            else:
                res.append(newInterval)
                newInterval = intervals[i]
        res.append(newInterval)
        return res

        