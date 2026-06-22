class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        visit = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        area,maxarea = 0,0 

        def dfs(r,c):
            #if already vsiite ddo not count
            if (r,c) in visit:
                return 0 
            visit.add((r,c))
            area = 1 
            for dr,dc in dirs:
                nr,nc = dr+r,dc+c
                if (0<=nr<row and 0<=nc<col and grid[nr][nc]==1 and (nr,nc) not in visit):
                    area+=dfs(nr,nc)
            
            return area 
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (r,c) not in visit:
                    area = dfs(r,c)
                    maxarea = max(area,maxarea)

        
        return maxarea