class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        l, r = 0,0
        longest_window = 1
        curr_window = set()
        while r < len(s):
            while s[r] in curr_window:
                curr_window.remove(s[l])
                l += 1
            longest_window = max(longest_window, (r-l+1))
            curr_window.add(s[r])
            r += 1
        
        return longest_window

        # abcabcbb
        # l
        #  r





        