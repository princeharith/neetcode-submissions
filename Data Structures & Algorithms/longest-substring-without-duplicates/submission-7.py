class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        l, r = 0,0
        maxLen = 0

        while r < len(s):
            counts[s[r]] += 1
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen

           
