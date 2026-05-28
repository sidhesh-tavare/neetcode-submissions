class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj =[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        q = deque()
        q.append((0,-1))
        visit.add(0)

        while q:
            curr,par = q.popleft()
            for nei in adj[curr]:
                if nei == par:
                    continue 
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei,curr))
        
        return len(visit) == n


        