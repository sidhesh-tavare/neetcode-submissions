class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)

        for i in range(1,n):
            ps,pe = res[-1]
            cs,ce = intervals[i]

            if cs<=pe:
                res[-1][0] = min(ps,cs)
                res[-1][1] = max(pe,ce)
            else:
                res.append(intervals[i])
        return res
        