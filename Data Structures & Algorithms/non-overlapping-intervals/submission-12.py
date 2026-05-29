class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        pe_max = res[-1][1]
        cnt=0
        for i in range(1,n):
            ps,pe = res[-1]
            cs,ce = intervals[i]

            if cs < pe_max:
                cnt+=1
                pe_max = min(ce,pe_max)
            else:
                pe_max = ce 
        return cnt

        