from collections import deque
INF = 2147483647
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        row,col = len(grid),len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    q.append((r,c))

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        while len(q)>0:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                
                if nr in range(row) and nc in range(col) and grid[nr][nc]==INF:
                    grid[nr][nc] = grid[r][c]+1
                    q.append((nr,nc))

        