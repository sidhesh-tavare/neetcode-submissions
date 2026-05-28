class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital,profits))
        projects.sort()

        from heapq import heapify, heappush as hpush, heappop as hpop
        max_heap = [] 
        n = len(projects)
        i = 0
        for _ in range(k):
            while i<n and projects[i][0]<=w:
                hpush(max_heap,-projects[i][1])
                i+=1
            
            if not max_heap:
                break

            w+= -hpop(max_heap)
        return w


