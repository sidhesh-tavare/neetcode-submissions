class Solution:
    from collections import deque 
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        lq = len(queries)
        if not prerequisites : return [False]*lq
        q = deque()
        adj = defaultdict(list)
        indeg = [0]*(numCourses)
        
        for pre,course in prerequisites:
            adj[pre].append(course)
            indeg[course]+=1
        
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        mp = defaultdict(set)

        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                mp[nei].add(curr)
                mp[nei].update(mp[curr])
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        
        return [course in mp[pre] for course,pre in queries]

        
        
