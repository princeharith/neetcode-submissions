class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        #in our recursive function
            #loop through every word in word dict
            #if its a valid word (check length and match)
            #AND if its substrings also match (call rescursion)
            #then return True
        
        memo = {len(s): True}
        def dfs(i):
            if i in memo:
                return memo[i]

            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)