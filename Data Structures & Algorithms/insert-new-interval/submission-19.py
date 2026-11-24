class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # 1--2
        #    2--4
        # 1-----4
        #         5--7
        
        i = 0
        res = []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            start = min(newInterval[0], intervals[i][0])
            end = max(newInterval[1], intervals[i][1])
            newInterval = [start, end]
            i += 1

        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
        

