class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        if origin == color : return image 
        from collections import deque
        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color
        row,col = len(image),len(image[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        while q:
            r,c = q.popleft()

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (0<=nr<row and 0<=nc<col and image[nr][nc]==origin):
                    image[nr][nc]=color
                    q.append((nr,nc))
        return image

        