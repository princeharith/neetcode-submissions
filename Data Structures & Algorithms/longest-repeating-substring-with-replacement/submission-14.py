class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #keep track of maxcount, by updating a max_count variable, check against the variable we just saw with p1
        #dont forget about stale counts! decrement as needed
        
        # k = 1
        # s = "XXYY"
        #         l
        #           r

        # maxcount = 2
        # max_substring = 3
        # char = Y
        # counts = {X: 1, Y: 2}

        maxcount = 0
        max_substring = 0
        l = 0
        counts = defaultdict(int)
        for r in range(len(s)):
            char = s[r]
            counts[char] += 1
            maxcount = max(maxcount, counts[char])
            while (r-l+1) - maxcount > k:
                counts[s[l]] -= 1
                l += 1
            
            max_substring = max(max_substring, (r-l+1))
        return max_substring
        

