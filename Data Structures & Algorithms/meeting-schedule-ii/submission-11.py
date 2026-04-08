"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #TODO - check edge cases
        if len(intervals) == 0:
            return 0

        

        # [(0,10), (1,40), (5,12), (11,30)]
        # endTimes = [10, 12, 40]
        # curr_rooms = 3


        # 0------10 11------30
        #     5------12
        #   1----------------------40
        

            
        curr_rooms = 1
        intervals.sort(key=lambda interval: interval.start)
        endTimes = [intervals[0].end]
        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            if curr_interval.start < endTimes[0]:
                #we have a conflict, keep the endTime
                curr_rooms += 1 
            else:
                heapq.heappop(endTimes)
            
            heapq.heappush(endTimes, curr_interval.end)
        
        return curr_rooms