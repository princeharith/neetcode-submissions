class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index_seen = {}
        
        for i, char in enumerate(s):
            last_index_seen[char] = i
        
        print(last_index_seen)

        start, end = 0, 0
        res = []
        for i, char in enumerate(s):
            end = max(last_index_seen[char], end)
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res


