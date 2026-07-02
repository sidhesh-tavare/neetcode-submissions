class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        from heapq import heapify, heappush as hpush, heappop as hpop
        adj = {}
        for i in range(n): adj[i] = []
        
        for s,d,w in edges:
            adj[s].append([d,w])  # adj[source] = [ [dest,weight],[dest,weight]]
        
        shortest = {} # map vertex => dist of shortest path
        minheap = [[0,src]] # distance , Source

        while minheap:
            w1,n1 = hpop(minheap)
            if n1 in shortest : continue 

            shortest[n1] = w1

            for n2,w2 in adj[n1]:
                if n2 not in shortest:
                    hpush(minheap,[w1+w2,n2])
        
        for i in range(n):
            if i not in shortest: shortest[i] = -1

        return shortest 

