class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        max_len = float('-inf')
        char_set = set()

        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max((r-l+1), max_len)
            r += 1
        
        return 0 if max_len == float('-inf') else max_len