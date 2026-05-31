class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up,down = 1,1 
        n = len(arr)
        best = 1 

        for i in range(1,n):
            prev,curr = arr[i-1],arr[i]

            if prev<curr:
                up = down + 1
                down = 1 
            elif prev>curr:
                down = up+1
                up = 1
            else:
                up,down =1,1
            best = max(best,up,down)
        return best
        