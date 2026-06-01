class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i,ch in enumerate(s):
            last[ch]=i 

        end = 0 
        start = 0 
        ans = []
        for i,ch in enumerate(s):
            end = max(end,last[ch])

            if i==end:
                ans.append(end-start+1)
                start = i+1
        return ans   
        