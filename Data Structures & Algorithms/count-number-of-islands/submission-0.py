class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        row,col = len(grid),len(grid[0])
        count = 0 
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            visit.add((r,c))
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if(nr in range(row) and nc in range(col) and grid[nr][nc]=="1" and (nr,nc) not in visit):
                    dfs(nr,nc)
            return
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visit:
                    count+=1
                    dfs(r,c)
        return count 
        