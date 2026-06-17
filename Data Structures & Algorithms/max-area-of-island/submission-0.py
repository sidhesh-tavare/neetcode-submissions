class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        visit = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        count = 0 

        def dfs(r,c):
            area = 1
            visit.add((r,c))
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if (nr in range(row) and nc in range(col)) and ((nr,nc) not in visit and grid[nr][nc]==1):
                    area+=dfs(nr,nc)
            
            return area

        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (r,c) not in visit:
                    temp = dfs(r,c)
                    count=max(temp,count)


        return count 

                    
        