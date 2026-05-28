from heapq import heappush as hpush, heappop as hpop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        res = []
        ctime = 0 
        tidx = 0 
        stasks = [[et,pt,idx] for idx,[et,pt] in enumerate(tasks)]
        stasks.sort()
        n = len(tasks)

        while tidx < n or heap:
            
            if not heap and ctime<stasks[tidx][0]:
                ctime = stasks[tidx][0]

            while tidx<n and ctime>=stasks[tidx][0]:
                st,pt,oidx = stasks[tidx]
                hpush(heap,[pt,oidx])
                tidx+=1
            
            pt,idx = hpop(heap)
            res.append(idx)
            ctime+=pt
        return res
        