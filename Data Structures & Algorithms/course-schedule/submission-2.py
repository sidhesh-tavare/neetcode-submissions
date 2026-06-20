from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indeg = [0]*(numCourses)

        for crs,pre in prerequisites:
            indeg[crs]+=1   # pre -> crs 
            adj[pre].append(crs)   # pre : crs 
        q = deque()
        
        for i in range(numCourses):
            if indeg[i]==0: 
                q.append(i)
        count = 0 

        while q:
            node = q.popleft()
            count+=1

            for nei in adj[node]:
                indeg[nei]-=1
                if indeg[nei] == 0:
                    q.append(nei)
            
        
        return numCourses==count
        