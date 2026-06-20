class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=(n-1): return False
        adj = defaultdict(list)
        visit = [0]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node,par):
            if visit[node]: return True 
            visit[node]=1
            for nei in adj[node]:
                if nei == par: continue
                if dfs(nei,node): return True 
            return False
        count = 0 
        for i in range(n):
            if not visit[i]:
                count+=1
                if count>1: return False
                if dfs(i,-1): return False
        return True