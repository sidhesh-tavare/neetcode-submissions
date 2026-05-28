class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pend = intervals[0][1]
        n = len(intervals)
        cnt=0
        for i in range(1,n):
            cs,ce = intervals[i]
            if cs<pend:
                cnt+=1
                pend=min(pend,ce)
            else:
                pend = ce 
        return cnt