class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pend = intervals[0][1]
        n = len(intervals)
        cnt=0
        #overlap condition cs<pe and since tehy are already arranged by the tsrat times its sorted 
        for i in range(1,n):
            cs,ce = intervals[i]
            if cs<pend: #we asre countinmg overlapping intervals we needto return the numbe rof intervals to delete so 
                cnt+=1
                pend=min(pend,ce)
            else:
                pend = ce 
        return cnt