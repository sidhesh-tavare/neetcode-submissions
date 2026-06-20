class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0]*numCourses
        adj = defaultdict(list)
        from collections import deque
        q = deque()
        count = 0 

        for course,pre in prerequisites:
            adj[pre].append(course)
            indeg[course]+=1
        
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
            
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            count+=1

            for nei in adj[node]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        
        if count!=numCourses:
            return []
        return res