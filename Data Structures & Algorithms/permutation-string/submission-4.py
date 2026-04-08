class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_counts = defaultdict(int)
        s2_counts = defaultdict(int)

        for char in s1:
            s1_counts[char] += 1

        for r in range(len(s2)):
            s2_counts[s2[r]] += 1
            if r-l+1 == len(s1):
                print(f'the s1 counts are {s1_counts}')
                print(f'the s2 counts are {s2_counts}')   
                if s1_counts == s2_counts:
                    return True
                s2_counts[s2[l]] -= 1
                if s2_counts[s2[l]] == 0:
                    del s2_counts[s2[l]]
                l += 1
        
        return False
            
        