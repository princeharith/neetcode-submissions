class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we get frequencies as we loop thru
        # if window - max freq seen <= k, we're good
        #otherwise we increment l, and remove from counts
        #update our max_freq

        counts = {}
        longest = 0

        l = 0

        def getMaxFreq(freqs):
            max_freq = 0
            for k, v in freqs.items():
                max_freq = max(v, max_freq)
            return max_freq


        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while (r-l+1) - getMaxFreq(counts) > k:
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
            
        