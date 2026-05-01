class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_counts = defaultdict(int)
        l = 0
        max_substring = 0
        max_freq = 0

        for r in range(len(s)):
            character_counts[s[r]] += 1
            max_freq = max(character_counts[s[r]], max_freq)
            while ((r-l+1) - max_freq) > k:
                character_counts[s[l]] -= 1
                l += 1
            max_substring = max(max_substring, (r-l+1))
   
        
        return max_substring
            
            

