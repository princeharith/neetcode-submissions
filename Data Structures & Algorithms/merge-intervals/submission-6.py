class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new_interval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_interval[1]:
                start = min(intervals[i][0], new_interval[0])
                end = max(intervals[i][1], new_interval[1])
                new_interval = [start, end]
            else:
                res.append(new_interval)
                new_interval = intervals[i]
        res.append(new_interval)
        return res
        #sort by start
        
        #use intervals 0 as a reference

        #loop from 1, len(intervals)

        #if merge, update new interval

        #otherwise, no merge. append to res, update new_interval

        #don't forget to append last interval 
