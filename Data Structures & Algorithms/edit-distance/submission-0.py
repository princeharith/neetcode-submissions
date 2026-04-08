class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dfs(index1, index2):
            if index1 == len(word1) and index2 == (len(word2)):
                return 0
            if index1 == len(word1):
                return len(word2)-index2
            if index2 == len(word2):
                return len(word1)-index1
            
            if (index1, index2) in cache:
                return cache[(index1, index2)]
                
            #replace
            replace = dfs(index1+1, index2+1)+1
            
            #deleted from word1
            delete = dfs(index1+1, index2)+1
            
            #inserted into word1
            insert = dfs(index1, index2+1)+1
            
            if word1[index1] == word2[index2]:
                match = dfs(index1+1, index2+1)
                cache[(index1, index2)] = min(match, replace, delete, insert)
                return min(match, replace, delete, insert)
            
            cache[(index1, index2)] = min(replace, delete, insert)
            return min(replace, delete, insert)
	

	
        return dfs(0,0)
	