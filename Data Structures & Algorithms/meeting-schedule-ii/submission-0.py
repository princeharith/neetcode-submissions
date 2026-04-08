"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = sorted(i.start for i in intervals)
        endTimes = sorted(i.end for i in intervals)
        
        s = e = 0
        maxCount, count = 0,0

        while s < len(intervals):
            if startTimes[s] < endTimes[e]:
                count += 1
                s+=1
            else:
                count -=1
                e+= 1
            maxCount = max(maxCount, count)
        
        return maxCount