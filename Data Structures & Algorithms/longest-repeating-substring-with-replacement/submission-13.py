class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)

        p1, p2 = 0,0
        max_count = 0
        chars_count = {}
        max_window = 0
        while p2 < len(s):
            char = s[p2]
            counts[char] += 1
            max_count= max(max_count, counts[char])

            while (p2-p1+1) - max_count > k:
                counts[s[p1]] -= 1
                p1 += 1
            
            max_window = max(max_window, (p2-p1+1))

            p2 += 1
        
        return max_window
        

            

        