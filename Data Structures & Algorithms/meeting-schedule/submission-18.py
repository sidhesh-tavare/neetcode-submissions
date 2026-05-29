"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        n = len(intervals)
        intervals = sorted([[i.start,i.end] for i in intervals])
        prevEnd = intervals[0][1]
        for i in range(1,n):
            cs,ce = intervals[i]
            if cs < prevEnd:
                return False
            prevEnd = max(ce,prevEnd)

        return True
            
