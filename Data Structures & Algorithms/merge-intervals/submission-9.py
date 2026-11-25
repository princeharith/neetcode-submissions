class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if not intervals:
            return []

        res = []
        prev_interval = intervals[0]

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            if curr_interval[0] <= prev_interval[1]:
                start = min(prev_interval[0], curr_interval[0])
                end = max(prev_interval[1], curr_interval[1])
                prev_interval = [start, end]
            else:
                res.append(prev_interval)
                prev_interval = curr_interval
        res.append(prev_interval)
        
        return res



        