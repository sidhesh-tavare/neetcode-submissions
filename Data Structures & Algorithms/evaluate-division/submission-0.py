class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        res = []
        for i in range(len(equations)):
            u,v = equations[i]
            weight = values[i]
            adj[u].append((v,weight))
            adj[v].append((u,1.0/weight))

        def dfs(node,target,visit):
            if node == target:
                return 1.0

            visit.add(node)

            for nei,weight in adj[node]:
                if nei not in visit:
                    result = dfs(nei,target,visit)

                    if result!=-1.0:
                        return weight*result 
            return -1.0

        
        for c,d in queries:
            if c not in adj or d not in adj:
                res.append(-1.0)
            elif c==d:
                res.append(1.0)
            else:
                visit = set()
                res.append(dfs(c,d,visit))

        return res