class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # 1--2
        #    2--4
        # 1-----4
        #           5--6
        
        res = []
        i = 0
        #case 1, current interval ends before new starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        #current doesn't end before new starts
        #we want to stop when newInterval < interval[i][0]
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res




        