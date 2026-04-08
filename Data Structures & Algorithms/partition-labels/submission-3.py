class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        interval_dict = {}
        res = []
        for i, char in enumerate(s):
            if char not in interval_dict:
                interval_dict[char] = [i,i]
            else:
                interval_dict[char][1] = i
        
        intervals = [[start, end] for _, (start, end) in interval_dict.items()]
        
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if prev[1] < intervals[i][0]:
                res.append(prev[1]-prev[0]+1)
                prev = intervals[i]
            elif intervals[i][0] < prev[1]:
                small =  min(intervals[i][0], prev[0])
                big = max(intervals[i][1], prev[1])
                prev = [small, big]
        res.append(prev[1]-prev[0]+1)
        return res