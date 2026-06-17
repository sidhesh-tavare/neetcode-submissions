from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0 
        fresh = 0 
        row,col = len(grid),len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(row):
            for c in range(col):
                if grid[r][c]==2: q.append((r,c))
                elif grid[r][c]==1: fresh+=1
        
        while q and fresh:
            level = len(q)

            for _ in range(level):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc=r+dr,c+dc
                    if (0<=nr<row and 0<=nc<col and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1


        if fresh: return -1 
        else: return time