class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPali(l,r,s):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
            return count


        #maxCount = 0
        res = 0
        for i in range(len(s)):
            evens = countPali(i, i, s)
            odds = countPali(i, i+1, s)

            res += evens
            res += odds

            #count = evens + odds
            #maxCount += count
            
        return res



        
        