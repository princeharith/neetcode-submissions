class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        #3 cases

        #case 1: endpoint of current interval < startpoint of new
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        
        #otherwise, we have a potential merge. endpoint of current interval is >= startpoint of new
        #we check if the endpoint of the newInterval >= startpoint of current
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i+=1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i+=1
        
        return res

        