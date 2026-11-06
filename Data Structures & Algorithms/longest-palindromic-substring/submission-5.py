class Solution:
    def longestPalindrome(self, s: str) -> str:

        #even odd

        res_index = 0
        res_len = 0

        for i in range(len(s)):
            #odd length palindrome
            l,r = i, i
            print(l,r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #found a bigger palindrome
                if (r-l+1) > res_len:
                    res_index = l
                    res_len = r-l+1

                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #found a bigger palindrome
                if (r-l+1) > res_len:
                    res_index = l
                    res_len = r-l+1

                l -= 1
                r += 1
        
    
        return s[res_index:res_index+res_len]


                
        
         