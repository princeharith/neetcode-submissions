class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_interval = intervals[0]
        res = 0

        # 1--2
        #    2--4
        # 1-----4
        

        for curr in intervals[1:]:
            if prev_interval[1] <= curr[0]:
                prev_interval = curr
            else:
                res += 1
                if prev_interval[1] > curr[1]:
                    prev_interval = curr
                    
                
        return res


        