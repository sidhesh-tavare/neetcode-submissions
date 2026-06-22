class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        row,col = len(grid),len(grid[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        # INF = land / 0 = Khajana / -1 = Water 
        from collections import deque
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            r,c = q.popleft()
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (0<=nr<row and 0<=nc<col and grid[nr][nc]==INF):
                    grid[nr][nc] = grid[r][c]+1
                    q.append((nr,nc))