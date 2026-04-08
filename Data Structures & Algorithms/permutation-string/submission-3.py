class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create a map for the count of chars in s1 
        #permuation will have the same count

        #loop through, increment l and r

        from collections import Counter

        s1_counts = Counter(s1)

        l, r = 0, len(s1)-1

        while r < len(s2):
            window_counts = Counter(s2[l:r+1])
            print(window_counts)
            if window_counts == s1_counts:
                return True
            l += 1
            r += 1
        
        return False
        