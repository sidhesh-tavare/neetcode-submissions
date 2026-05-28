from heapq import heappush_max as hpush, heappop_max as hpop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        res = []
        if a > 0: hpush(heap, [a, "a"])
        if b > 0: hpush(heap, [b, "b"])
        if c > 0: hpush(heap, [c, "c"])

        while heap:
            c1,ch1=hpop(heap)
            if len(res)>=2 and res[-1]==ch1 and res[-2]==ch1:

                if not heap:
                    break

                c2,ch2= hpop(heap)
                if c2>0:
                    res.append(ch2)
                    c2-=1
                if c2>0:
                    hpush(heap,[c2,ch2])
                hpush(heap,[c1,ch1])
            else:
                res.append(ch1)
                c1-=1
                if c1>0:
                    hpush(heap,[c1,ch1])
        
        return "".join(res)
                

        