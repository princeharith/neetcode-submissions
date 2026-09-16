class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        for c in s1:
            count1[c] += 1

        need = len(count1)
        for i in range(len(s2)):
            count2 = defaultdict(int)
            cur = 0
            for j in range(i, len(s2)):
                char = s2[j]
                count2[char] += 1
                #adding that char made the counts in count2 higher
                if count1[char] < count2[char]:
                    break
                if count1[char] == count2[char]:
                    cur += 1
                
                if need == cur:
                    return True
        return False

        
