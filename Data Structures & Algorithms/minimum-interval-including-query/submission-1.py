from heapq import heapify, heappush as hpush, heappop as hpop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        q = len(queries)
        intervals.sort()
        s_queries = sorted([(q,i) for i,q in enumerate(queries)])
        res = [-1]*q
        heap = []
        i = 0 

        for query,oidx in s_queries:

            while i<n and intervals[i][0]<=query:
                s,e = intervals[i]
                hpush(heap,(e-s+1,e))
                i+=1
            
            while heap and heap[0][1] < query:
                hpop(heap)

            if heap:
                res[oidx]=heap[0][0]
            else:
                res[oidx]=-1
        return res
            
