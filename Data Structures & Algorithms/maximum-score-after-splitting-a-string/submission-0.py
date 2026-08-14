class Solution:
    def maxScore(self, s: str) -> int:
        ones_count = s.count('1')
        zero_count = 0
        total_score = 0

        for i in range(len(s)-1):
            if s[i] == '0':
                zero_count += 1
            elif s[i] == '1':
                ones_count -= 1
            print(ones_count, zero_count)
            total_score = max(total_score, zero_count+ones_count)
        
        return total_score
