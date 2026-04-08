class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                res += 1
            else:
                prev = intervals[i]
        
        return res