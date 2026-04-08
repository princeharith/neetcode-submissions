class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        def dfs(i, j):
            if (i+j) == len(s3):
                return (i == len(s1)) and (j == len(s2))
            
            if i < len(s1) and s1[i] == s3[i+j]:
                if dfs(i + 1, j):
                    return True
            
            if j < len(s2) and s2[j] == s3[i+j]:
                if dfs(i, j + 1):
                    return True
            
            return False
        
        return dfs(0, 0)