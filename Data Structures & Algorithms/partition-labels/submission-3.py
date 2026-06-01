class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        res = []
        for i,ch in enumerate(s):
            last[ch]=i
        
        end,start =0,0
        for i,ch in enumerate(s):
            end = max(end,last[ch])

            if i==end:
                res.append(end-start+1)
                start=end+1
        return res

        