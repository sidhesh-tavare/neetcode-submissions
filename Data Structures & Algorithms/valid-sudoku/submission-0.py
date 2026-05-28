class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]  
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue 
                
                square_index = (i // 3) * 3 + (j // 3)  

                # ROW CHECK
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # COLUMN CHECK
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # 3x3 BOX CHECK
                if num in squares[square_index]:
                    return False
                squares[square_index].add(num)

        return True


            
            

        