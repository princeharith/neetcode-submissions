class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        unique_chars = set(t)
        freq_t = [0] * 52
        for char in t:
            freq_t[ord(char) - ord('a')] += 1
        
        curr_freq = [0] * 52
        curr_matches = 0
        l = 0

        shortest_substring = ''
        len_shortest_substring = float('inf')
        shortest_substring_indices = []
        matches = 0

        #curr_freq = [0,0,0,0,1,0,0,]
        for r in range(len(s)):
            curr_freq[ord(s[r]) - ord('a')] += 1
            
            if curr_freq[ord(s[r]) - ord('a')] == freq_t[ord(s[r]) - ord('a')]:
                matches += 1

            while matches == len(unique_chars):
                #check the current window
                if (r-l+1) < len_shortest_substring:
                    len_shortest_substring = (r-l+1)
                    shortest_substring_indices = [l,r+1]

                curr_freq[ord(s[l]) - ord('a')] -= 1
                if curr_freq[ord(s[l]) - ord('a')] < freq_t[ord(s[l]) - ord('a')]:
                    matches -= 1
                l += 1
        
        if len_shortest_substring == float('inf'):
            return ''
        
        start, stop = shortest_substring_indices
        return s[start:stop]
        




