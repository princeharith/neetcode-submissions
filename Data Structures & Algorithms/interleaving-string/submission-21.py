class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]

            if (i+j) == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[i+j]:
                if dfs(i + 1, j):
                    cache[(i,j)] = True
                    return True
            
            if j < len(s2) and s2[j] == s3[i+j]:
                if dfs(i, j + 1):
                    cache[(i,j)] = True
                    return True
            
            cache[(i, j)] = False
            return False
        
        return dfs(0, 0)