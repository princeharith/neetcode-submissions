class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        #for odd length palindromes
        max_len = 1
        palindrome = s[0]
        for i in range(1,len(s)):
            l, r = i-1, i+1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r-l+1) > max_len:
                        max_len = r-l+1
                        palindrome = s[l:r+1]                    
                    l -= 1
                    r += 1
                else:
                    break
            


        for i in range(len(s)):
            l, r = i, i+1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if (r-l+1) > max_len:
                        max_len = r-l+1
                        palindrome = s[l:r+1]                    
                    l -= 1
                    r += 1
                else:
                    break
        
        return palindrome

        