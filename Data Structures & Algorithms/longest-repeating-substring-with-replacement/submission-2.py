class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)

        l,r = 0,0
        maxLen = 0

        def getMaxFreq(count):
            maxfreq = 0
            for k,v in count.items():
                maxfreq = max(maxfreq, v)
            return maxfreq

        while r < len(s):
            counts[s[r]] += 1
            while (((r-l)+1 - getMaxFreq(counts)) > k):
                counts[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen