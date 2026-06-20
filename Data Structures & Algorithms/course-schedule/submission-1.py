class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for crs,pre in prerequisites:
            adj[crs].append(pre)
        visit = set()

        def dfs(crs):
            #if safe return TRUE
            if crs in visit: return False
            if adj[crs]==[]: return True 
            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True 
        