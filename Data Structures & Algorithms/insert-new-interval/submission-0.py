class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort()
        res.append(intervals[0])
        n = len(intervals)
        for i in range(1,n):
            ps,pe = res[-1]
            cs,ce = intervals[i]
            if cs in range(ps,pe+1):
                res[-1][0] = min(ps,cs)
                res[-1][1] = max(pe,ce)
            else:
                res.append(intervals[i])

        return res
        
        