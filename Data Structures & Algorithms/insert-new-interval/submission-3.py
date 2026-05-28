class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for i in range(1,n):
            ps,pe = res[-1]
            cs,ce = intervals[i]

            if cs<=pe:
                res[-1][1] = max(pe,ce)
            else:
                res.append(intervals[i])
        return res
        