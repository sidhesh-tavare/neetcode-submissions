class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first , last = {}, {}
        intervals = []
        merged = []
        res = []    

        for i,ch in enumerate(s):
            if ch not in first:
                first[ch]=i
            last[ch]=i
        for ch in first:
            intervals.append([first[ch],last[ch]])

        intervals.sort()
        merged = [intervals[0]]

        for i in range(1,len(intervals)):
            cs,ce = intervals[i]
            ps,pe = merged[-1]
            if cs<=pe:
                merged[-1][1]= max(ce,pe)
            else:
                merged.append(intervals[i])

        for s,e in merged:
            res.append(e-s+1)
        
        return res
                
        