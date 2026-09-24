class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # s = "AAAAAAABAAAAAAAAAAA" k = 0
        #       l
        #             r

        l = 0
        counts = defaultdict(int)
        max_count = 0
        max_window = 0
       

        for r in range(len(s)):
            letter = s[r]
            counts[s[r]] += 1
            max_count = max(max_count, counts[s[r]])

            while (r-l+1) - max_count > k:
                counts[s[l]] -= 1
                l += 1
            
            max_window = max(r-l+1, max_window)
        
        return max_window

                
