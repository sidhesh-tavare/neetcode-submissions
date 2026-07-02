from math import inf 
from heapq import heapify, heappush as hpu, heappop as hpo, heappush_max as hpum, heappop_max as hpom
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        dist = [inf]*(n+1)
        for u,v,w in times: adj[u].append((v,w))
        pq = [(0,k)]
        dist[k] = 0

        while pq:
            curr_wt,curr_node = hpo(pq)
            
            if curr_wt > dist[curr_node]: continue

            for next_node,next_wt in adj[curr_node]:
                if curr_wt + next_wt < dist[next_node]:
                    dist[next_node] = curr_wt+next_wt
                    hpu(pq,(dist[next_node],next_node))
        
        ans = 0 
        for i in range(1,n+1):
            if dist[i] == inf: return -1
            ans = max(ans,dist[i])
        print(ans)
        print(dist)
        return ans


        