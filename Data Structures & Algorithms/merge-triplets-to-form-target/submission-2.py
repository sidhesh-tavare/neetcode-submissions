class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta,tb,tc = target
        triplets.sort()
        ar,br,cr=[],[],[]
        ma,mb,mc = 0,0,0
        for a,b,c in triplets:
            if a<=ta and b<=tb and c<=tc:
                ar.append(a)
                br.append(b)
                cr.append(c)
                ma,mb,mc = max(ma,a),max(mb,b),max(c,mc)
        
        if (ma==ta and mb==tb and mc==tc):
            return True
        return False 