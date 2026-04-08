class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        path = set()

        def dfs(r,c,index):
            if len(word) == index:
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in path or word[index] != board[r][c]:
                return False
            
            path.add((r,c))
            
            res = dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or dfs(r, c+1, index+1) or dfs(r, c-1, index+1)

            path.remove((r,c))

            return res
            
           

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
