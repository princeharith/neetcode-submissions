class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "zxyzxyz"
        #  l
        #   r

         #we init our pointers for window

         #while r < length of string
            #add to our window 
            #if s[r] is in the window, we increment l and update window
            #check against global window size
        
        #return our longest window

        #condition if length is 0 or 1
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        l, r = 0, 1
        longest_window = 1
        curr_window = set(s[0])
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





        