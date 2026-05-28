from heapq import heappush as hpush, heappop as hpop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ctime = 0 
        heap = []
        res = []
        taskidx = 0 
        n = len(tasks)

        stasks = sorted([[t[0],t[1],idx] for idx,t in enumerate(tasks)])

        while taskidx<n or heap:
            # while theq is empoty and tehre are no task in it forard the ctime to match the shortest enqueue time 
            if not heap and ctime<stasks[taskidx][0]:
                ctime =  stasks[taskidx][0]
            
            while taskidx < n and stasks[taskidx][0]<=ctime:
                st,pt,oidx = stasks[taskidx]
                hpush(heap,[pt,oidx])
                taskidx+=1

            pt,oidx = hpop(heap)
            res.append(oidx)
            ctime+=pt
        return res