"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 0--2
        #   1--3
        #     2--4
        #      3--5
        # heap = [2, 3]
        #if current_interval's start is >= heap[0] #heap keeps track of end times
        #then we pop
        #number of intervals in our heap is number of rooms needed (unpopped)
        intervals.sort(key=lambda x: x.start)
        min_heap = []


        for interval in intervals:
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap) 
       

        