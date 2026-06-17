class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapper = defaultdict(int)
        for src,dst in trust:
            mapper[src]-=1
            mapper[dst]+=1
        
        for i in range(1,n+1):
            if mapper[i] == n-1: return i 
        return -1
        