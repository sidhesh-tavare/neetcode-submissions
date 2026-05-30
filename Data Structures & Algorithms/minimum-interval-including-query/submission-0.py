from heapq import heapify, heappush as hpush , heappop as hpop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Instead of queries.sort()
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        intervals.sort()
        inters = []
        n = len(intervals)
        q = len(queries)
        i = 0 
        res = [-1]*q

        for query,idx in sorted_queries:

            while i<n and intervals[i][0]<= query:
                s,e = intervals[i]
                hpush(inters,(e-s+1,e))
                i+=1

            while inters and inters[0][1] < query:
                lenn,endd = hpop(inters)
            
            if inters:
                res[idx]=inters[0][0]
            else:
                res[idx]=-1
        return res
            


