class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        rows = [0]*row
        cols = [0]*col

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    rows[r]+=1
                    cols[c]+=1
        
        cnt = 0 

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (rows[r]>1 or cols[c]>1):
                    cnt+=1
        return cnt
        