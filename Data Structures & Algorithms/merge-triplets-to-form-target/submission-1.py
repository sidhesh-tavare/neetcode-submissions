class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta,tb,tc = target
        triplets.sort()
        ar,br,cr=[],[],[]
        for a,b,c in triplets:
            if a<=ta and b<=tb and c<=tc:
                ar.append(a)
                br.append(b)
                cr.append(c)
        
        if (ar and br and cr):
            if max(ar)==ta and max(br)==tb and max(cr)==tc:
                return True
        return False