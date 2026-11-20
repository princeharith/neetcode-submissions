class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand(l,r):
            curr_count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_count += 1
                l -= 1
                r += 1
            return curr_count

        
        #odd_length
        i = 0
        count = 0
        while i < len(s):
            l,r = i,i
            count += expand(l,r)
            i += 1
        
        #even_length
        i = 0
        while i+1 < len(s):
            l,r = i, i+1
            count += expand(l,r)
            i += 1
        
        return count
            
        