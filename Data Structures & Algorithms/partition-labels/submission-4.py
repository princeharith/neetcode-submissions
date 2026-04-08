class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen_idx = {char:i for i, char in enumerate(s)}
        start, end = 0,0
        res = []
        for i, char in enumerate(s):
            end = max(end, last_seen_idx[char])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        
        return res

        