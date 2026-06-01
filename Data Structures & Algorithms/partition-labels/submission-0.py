class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first,last ={},{}
        n = len(s)
        for i,ch in enumerate(s):
            if ch not in first:
                first[ch] = i 
            last[ch] = i
        
        intervals = []

        for ch in first:
            intervals.append([first[ch],last[ch]])
        
        intervals.sort()

        res = [intervals[0]]

        for i in range(1,len(intervals)):
            cs,ce = intervals[i]
            ps,pe = res[-1]
            if cs<=pe:
                res[-1][1]=max(ce,pe)
            else:
                res.append(intervals[i])
        
        ans = []
        for s,e in res:
            ans.append(e-s+1)
        return ans
        