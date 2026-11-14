"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #given intervals, out of order
            #sort by start/end? 
        #same number not considered a conflict
        
        #intervals =  (2,5), (5,7), (9,10)

        #0----------10
        #  2---5
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)-1):
            curr_interval = intervals[i]
            next_interval = intervals[i+1]

            if curr_interval.end > next_interval.start:
                return False
        
        return True


