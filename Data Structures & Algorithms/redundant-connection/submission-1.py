class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = [0]*(n+1)
        cycle = set()
        start = -1 

        def dfs(node,par):
            nonlocal start 
            if visit[node]:
                start = node 
                return True 
            visit[node]= 1 

            for nei in adj[node]:
                if nei == par: continue 
                if dfs(nei,node):
                    if start!=-1:
                        cycle.add(node)
                    if node == start:
                        start=-1
                    return True 
            return False 
        
        dfs(1,-1)

        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        
        return []
        
