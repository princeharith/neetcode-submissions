class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda intervals: intervals[0])

        num_removed = 0
        #res = [intervals[0]]
        prevEnd = intervals[0][1]
        for start,end in intervals[1:]:
            if prevEnd > start:
                num_removed += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        
        return num_removed


        