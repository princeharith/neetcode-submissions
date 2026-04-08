class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def search(i,j,k):
            if k == len(word):
                return True
            #conditions -> if new r and new c are in bounds
            #if point in visited
            #if word doesnt equal k
            if (
                i < 0 or 
                i >= len(board) or
                j < 0 or
                j >= len(board[0]) or
                (i,j) in visited or
                board[i][j] != word[k]
            ):
                return False

            visited.add((i,j))

            found = (
                search(i+1,j,k+1) or 
                search(i-1,j,k+1) or 
                search(i,j+1,k+1) or
                search(i,j-1,k+1)
            )

            visited.remove((i,j))

            return found
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i,j,0):
                    return True
        
        return False
                