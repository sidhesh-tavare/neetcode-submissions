from heapq import heapify,heappush as hpush , heappop as hpop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n,s = len(hand),groupSize
        if n%s!=0: return False
        mapper = Counter(hand)
        heap = list(mapper.keys())
        heapify(heap)

        while heap:
            smallest = heap[0]

            if mapper[smallest]==0:
                hpop(heap)
                continue
            
            for i in range(s):
                next_card = smallest+i
                if mapper[next_card] == 0:
                    return False
                else:
                    mapper[next_card]-=1
        
        return True 
            



        
        