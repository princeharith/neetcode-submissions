class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        #3 sets for each thing we track
            #col, posDiag, negDiag (since we loop thru rows)
        colSet = set()
        posDiag = set()
        negDiag = set()
        board = [['.'] * n for _ in range(n)]

        res = []
        
        #backtracking function, we only need to take in the row
            #base case, row == n
            #add our copy to res
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            
            for c in range(n):
                if c in colSet or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                colSet.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)
                board[r][c] = '.'
                colSet.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        backtrack(0) 
        return res

        
        #for each col
            #check if this is valid, if not return
        
        #Add to our sets, add the Q at this coordinate
        #call backtrack on the next row

        #Clean up for next iteration for col





                

