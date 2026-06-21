class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1: return [0]
        adj = defaultdict(list)
        deg = [0]*n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u]+=1
            deg[v]+=1
        
        from collections import deque
        q = deque()

        for i in range(n):
            if deg[i]==1:
                q.append(i)
        
        node = n 

        while node>2:
            count = len(q)
            node-=count

            for _ in range(count):
                leaf = q.popleft()
                deg[leaf]-=1
                for nei in adj[leaf]:
                    deg[nei]-=1

                    if deg[nei]==1:
                        q.append(nei)
        
        return list(q)
            


        
        