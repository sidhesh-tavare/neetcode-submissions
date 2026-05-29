"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush as hpush , heappop as hpop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted([[i.start,i.end] for i in intervals])
        rooms = []
        n = len(intervals)
        if n==1: return 1 
        if n==0 : return 0 
        hpush(rooms,intervals[0][1])

        for i in range(1,n):
            #curr start >= prev end => pop
            if intervals[i][0]>=rooms[0] :
                hpop(rooms)
            hpush(rooms,intervals[i][1])
        return len(rooms)
        
        