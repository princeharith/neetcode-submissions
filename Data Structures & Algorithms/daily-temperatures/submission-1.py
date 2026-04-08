class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        #stack.append((temperatures[0], 0))
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, j = stack.pop()
                res[j] = index - j
            stack.append((temp, index))
        
        return res