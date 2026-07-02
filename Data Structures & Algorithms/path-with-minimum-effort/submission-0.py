from heapq import heapify, heappush as hpu, heappop as hpo 
from math import inf
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col = len(heights),len(heights[0])
        dist = [ [inf]*(col) for _ in range(row)]
        dist[0][0] = 0 
        pq = [(0,0,0)] # dist , source, destination
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        
        while pq:
            curr_dist,cr,cc = hpo(pq) # current row , current col 

            if curr_dist > dist[cr][cc] : continue 

            for dr,dc in dirs:
                nr,nc = cr+dr,cc+dc
                if (0<=nr<row and 0<=nc<col):
                    step_dist = abs(heights[nr][nc] - heights[cr][cc])
                    total_dist = max(curr_dist,step_dist)

                    if total_dist < dist[nr][nc]:
                        dist[nr][nc] = total_dist
                        hpu(pq,(total_dist,nr,nc))

        
        return dist[row-1][col-1]

        