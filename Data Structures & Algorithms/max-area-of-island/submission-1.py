class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        maxarea = 0 

        def dfs(r,c):

            if grid[r][c]==0: return 0 
            area = 1 
            grid[r][c]=0
            if r>0: area+=dfs(r-1,c)
            if r<row-1 : area +=dfs(r+1,c)
            if c>0: area+=dfs(r,c-1)
            if c<col-1: area+=dfs(r,c+1)

            return area 

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    maxarea = max(area,maxarea)
        
        return maxarea