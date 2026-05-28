"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True 
        intervals = [[inte.start,inte.end] for inte in intervals]
        intervals.sort()
        n = len(intervals)
        pend = intervals[0][1]
        for i in range(1,n):
            cs,ce = intervals[i]
            if cs<pend:
                return False
            pend = ce
        return True
