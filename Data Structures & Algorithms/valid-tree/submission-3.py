class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=(n-1): return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def hascycle(node,par):
            if node in visit: return True 
            visit.add(node)
            for nei in adj[node]:
                if nei == par: continue 
                if hascycle(nei,node): return True 

            return False

        if hascycle(0,-1):
            return False
        if len(visit)!=n: return False
        return True 
        