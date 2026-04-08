class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def dfs(index1, index2):
            # if index1 == len(s1) and index2 == len(s2):
            #     return index1 + index2 == len(s3)
            if index1 + index2 == len(s3):
                return index1 == len(s1) and index2 == len(s2)
            
            if (index1, index2) in cache:
                return cache[(index1, index2)]

            #take from s1
            if index1 < len(s1):
                if s1[index1] == s3[index1+index2]:
                    if dfs(index1+1, index2):
                        cache[(index1, index2)] = True
                        return True
            #otherwise try s2
            if index2 < len(s2):
                if s2[index2] == s3[index1+index2]:
                    if dfs(index1, index2+1):
                        cache[(index1, index2)] = True
                        return True
            cache[(index1, index2)] = False
            return False
    

        return dfs(0,0)
        